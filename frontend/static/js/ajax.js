async function load_data() {
	console.log(window.isClick);
	if(!window.isClick){
		fetch('http://127.0.0.1:5000/api/'+window.model, { method: "GET",mode: 'cors' })
			.then((response) => {return response.json()})
			.then((jsonData) => {inject_html(jsonData);window.data=jsonData;})//講資料植入html)
			.catch((err) => {
				console.log('錯誤:', err);
				return jsonData;
			});
	}
}
// window.onclick=console.log(1);

window.isClick=false;
window.onload = ()=>{window.model='machine';load_data();set('machine')};
window.setInterval(load_data,5000);//auto reload 

function delete_data(id) {
	console.log(id);
	fetch('http://127.0.0.1:5000/api/'+window.model, { method: 'DELETE', body: "key=_id&value=" + id, headers: { 'Content-Type': 'application/x-www-form-urlencoded' } })
		.then(() => { let users = document.getElementById('users'); users.innerHTML = ''; load_data() });
	let modalEl = document.getElementById('exampleModal' + id);
	let mymodal = bootstrap.Modal.getInstance(modalEl);
	mymodal.hide();
	window.isClick=false;
}

function generate_modal(id){
	data='<td>\
	<button type="button" class="btn btn-danger " onclick="window.isClick=true;" data-bs-toggle="modal" data-bs-target="#exampleModal'+ id + '">刪除</button>\
	<div class="modal fade" id="exampleModal'+ id + '" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">\
		<div class="modal-dialog">\
			<div class="modal-content">\
				<div class="modal-header">\
					<h5 class="modal-title" id="exampleModalLabel">確認刪除？</h5>\
					<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>\
				</div>\
				<div class="modal-body">\
					<p class="fw-bold">請注意！刪除後將無法復原！</p>\
				</div>\
				<div class="modal-footer">\
					<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">取消</button>\
					<button type="button" class="btn btn-danger" onclick="delete_data(\''+ id + '\')" >確認刪除</button>\
				</div>\
			</div></div></div></td></tr>';
	return data;
}

function inject_html(data) {
	// console.log(data)
	let users = document.getElementById('users');
	let title = document.getElementById('title');
	let label = document.getElementById('label');
	label.innerText=window.model;
	users.innerHTML = '';
	// console.log(model)

	//generate title
	if(window.model=='machine')
		title_label=['_id','type','status','ip','mac','delete']
	else if (window.model=='user')
		title_label=['_id','name','phone','license_plate','delete']
	else
		title_label=['_id','status','license_plate','position','machine','delete'];

	title.innerHTML='';
	for(let k in title_label)
		title.innerHTML+='<th scope="col" style="min-height:100px!important;">'+title_label[k]+'</th>';

	for (let i = 0; i < data.length; i++) {
		// console.log(data[i].length);
		if (window.model=='machine')
		{
			status_tag='';
			if (data[i]['status']=='alive')
				status_tag='<td style="color:green"><ion-icon name="radio-button-on-outline" style="font-size:10px"></ion-icon> alive</td>';
			else
				status_tag='<td style="color:red"><ion-icon name="radio-button-on-outline" style="font-size:10px"></ion-icon> lost</td>';
			pre_fill="<tr><td><a href='/" + data[i]['_id'] + "'>" + data[i]['_id'] + "</a></td><td>" + data[i]["type"] + "</td>"+ status_tag + "<td>" + data[i]["ip"] + "</td><td>" + data[i]["mac"] + '</td>';
		}else if(window.model=='user'){
			pre_fill="<tr><td>" + data[i]['_id'] + "</td><td><a href='/" + data[i]['_id'] + "'>" + data[i]["name"] + "</a></td><td>" + data[i]["phone"] + "</td><td>" + data[i]["license_plate"] + '</td>';
		}else if (window.model=='parking'){
			if (data[i]['status']=='empty')
				status_tag='<td style="color:green"><ion-icon name="radio-button-on-outline" style="font-size:10px"></ion-icon> empty</td>';
			else
				status_tag='<td style="color:red"><ion-icon name="radio-button-on-outline" style="font-size:10px"></ion-icon> inuse</td>';
			pre_fill="<tr><td><a href='/" + data[i]['_id'] + "'>" + data[i]['_id'] + "</a></td>" + status_tag + "<td>" + data[i]["license_plate"] + "</td><td>" + data[i]["position"] + "</td><td>" + data[i]["machine"] + '</td>';
		}
		pre_fill+=generate_modal(data[i]['_id']);
		users.innerHTML += pre_fill;
	}
}

async function set(model,mode='list'){
	window.model=model;
	button_nav=document.getElementById('button-nav');
	if (model=='parking')
	{
		button_nav.innerHTML='\
		<li class="nav-item me-2 ">\
			<a class="nav-link" href="#"  id="label" style="width: 100px" onclick="set(\''+model+'\',\'list\')" ></a>\
		</li>\
		<li class="nav-item me-2 " >\
			<a class="nav-link" href="#" style="width: 100px" onclick="set(\''+model+'\',\'map\')"  >map</a>\
		</li>';
	}else{
		button_nav.innerHTML='\
		<li class="nav-item me-2 ">\
			<a class="nav-link" href="#"  id="label" style="width: 100px" ></a>\
		</li>';
	}

	main_content=document.getElementById('main-content');
	if (mode=='list'){
		main_content.innerHTML='                    \
		<table class=" table text-start ">\
		<thead style="width: 100%;position:sticky !important;"><tr id="title" ></tr></thead>\
		<tbody id="users" style="word-break:keep-all;max-height:550px!important;overflow-y:scroll">\
		</tbody></table>';
	}else{
		main_content.innerHTML='<div id="map"></div>';
		await load_data();
		console.log(window.data);
		initMap(window.data);

	}
	load_data();
}

function insert_user() {
	fetch('http://127.0.0.1:5000/api/manage', { method: 'POST', body: 'name=' + document.getElementById('name').value + '&place=' + document.getElementById('place').value+'&jointime=' + document.getElementById('jointime').value + '&cardid=' + document.getElementById('cardid').value, headers: { 'Content-Type': 'application/x-www-form-urlencoded' } })
		.then(() => { let users = document.getElementById('users'); users.innerHTML = ''; load_data() });

}

// function search() {
// 	key = document.getElementById('key').value;
// 	value = document.getElementById('value').value;
// 	fetch('http://127.0.0.1:8000api/manage?' + new URLSearchParams({ 'key': key, 'value': value }), {})
// 		.then((response) => (response.json()))
// 		.then(res => (inject_html(res)))
// }
