
function load_data() {
	fetch('http://127.0.0.1:8000/api/'+window.model, { method: "GET",mode: 'cors' })
		.then((response) => {console.log(response);return response.json()})
		.then((jsonData) => (inject_html(jsonData)))//講資料植入html
		.catch((err) => {
			console.log('錯誤:', err);
		});
}
window.onload = ()=>{window.model='machine';load_data()};

function delete_user(model='machine',id) {
	fetch('http://127.0.0.1:8000/api/'+model, { method: 'DELETE', body: "key=_id&value=" + id, headers: { 'Content-Type': 'application/x-www-form-urlencoded' } })
		.then(() => { let users = document.getElementById('users'); users.innerHTML = ''; load_data() });
	let modalEl = document.getElementById('exampleModal' + id);
	let mymodal = bootstrap.Modal.getInstance(modalEl);
	mymodal.hide();
}

// function insert_user() {
// 	fetch('http://127.0.0.1:8000/api/manage', { method: 'POST', body: 'name=' + document.getElementById('name').value + '&place=' + document.getElementById('place').value+'&jointime=' + document.getElementById('jointime').value + '&cardid=' + document.getElementById('cardid').value, headers: { 'Content-Type': 'application/x-www-form-urlencoded' } })
// 		.then(() => { let users = document.getElementById('users'); users.innerHTML = ''; load_data() });

// }

// function search() {
// 	key = document.getElementById('key').value;
// 	value = document.getElementById('value').value;
// 	fetch('http://127.0.0.1:8000api/manage?' + new URLSearchParams({ 'key': key, 'value': value }), {})
// 		.then((response) => (response.json()))
// 		.then(res => (inject_html(res)))
// }

function inject_html(data) {
	console.log(data)
	let users = document.getElementById('users');
	let title = document.getElementById('title');
	let label = document.getElementById('label');
	label.innerText=window.model;
	users.innerHTML = '';

	for (let i = 0; i < data.length; i++) {
		console.log(data[i].length)
		// work=jsonData[i].work;
		if (window.model=='machine')
		{
			//change title
			title_label=['_id','type','status','position','ip','mac','delete']
			title.innerHTML='';
			for(let k in title_label)
			{
				title.innerHTML+='<th scope="col" style="min-height:100px!important;">'+title_label[k]+'</th>';
			}
			users.innerHTML += "<tr><td>" + data[i]['_id'] + "</td><td><a href='/" + data[i]['_id'] + "'>" + data[i]["type"] + "</a></td><td>" + data[i]["status"] + "</td><td>" + data[i]["position"] + "</td><td>" + data[i]["ip"] + "</td><td>" + data[i]["mac"] + '</td>\
			<td>\
			<button type="button" class="btn btn-danger" data-bs-toggle="modal"\
				data-bs-target="#exampleModal'+ data[i]['_id'] + '">刪除</button>\
			<div class="modal fade" id="exampleModal'+ data[i]['_id'] + '" tabindex="-1"\
				aria-labelledby="exampleModalLabel" aria-hidden="true">\
				<div class="modal-dialog">\
					<div class="modal-content">\
						<div class="modal-header">\
							<h5 class="modal-title" id="exampleModalLabel">確認刪除？</h5>\
							<button type="button" class="btn-close" data-bs-dismiss="modal"\
								aria-label="Close"></button>\
						</div>\
						<div class="modal-body">\
							<p class="fw-bold">請注意！刪除後將無法復原！</p>\
						</div>\
						<div class="modal-footer">\
							<button type="button" class="btn btn-secondary"\
								data-bs-dismiss="modal">取消</button>\
							<button type="button" class="btn btn-danger"\
								onclick="delete_user('+ data[i]['_id'] + ')" >確認刪除</button>\
						</div>\
					</div>\
				</div>\
			</div>\
			</td></tr>';
		}else if(window.model=='user'){
			//change title
			title_label=['_id','name','phone','license_plate','delete']
			title.innerHTML='';
			for(let k in title_label)
			{
				title.innerHTML+='<th scope="col" style="min-height:100px!important;">'+title_label[k]+'</th>';
			}


			users.innerHTML += "<tr><td>" + data[i]['_id'] + "</td><td><a href='/" + data[i]['_id'] + "'>" + data[i]["name"] + "</a></td><td>" + data[i]["phone"] + "</td><td>" + data[i]["license_plate"] + '</td>\
			<td>\
			<button type="button" class="btn btn-danger" data-bs-toggle="modal"\
				data-bs-target="#exampleModal'+ data[i]['_id'] + '">刪除</button>\
			<div class="modal fade" id="exampleModal'+ data[i]['_id'] + '" tabindex="-1"\
				aria-labelledby="exampleModalLabel" aria-hidden="true">\
				<div class="modal-dialog">\
					<div class="modal-content">\
						<div class="modal-header">\
							<h5 class="modal-title" id="exampleModalLabel">確認刪除？</h5>\
							<button type="button" class="btn-close" data-bs-dismiss="modal"\
								aria-label="Close"></button>\
						</div>\
						<div class="modal-body">\
							<p class="fw-bold">請注意！刪除後將無法復原！</p>\
						</div>\
						<div class="modal-footer">\
							<button type="button" class="btn btn-secondary"\
								data-bs-dismiss="modal">取消</button>\
							<button type="button" class="btn btn-danger"\
								onclick="delete_user('+ data[i]['_id'] + ')" >確認刪除</button>\
						</div>\
					</div>\
				</div>\
			</div>\
			</td></tr>';
		}
	}
}

function set(model){
	window.model=model;
	load_data();
}