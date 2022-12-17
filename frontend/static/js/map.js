function initMap(data) {
    console.log('init')
    var markers = [];
    var infoWindows = [];
    //設定中心點
    var map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: 25.04, lng: 121.512 },
        zoom: 14
    });
    var geocoder = new google.maps.Geocoder();
    console.log(geocoder);

    var info_config = [];
    var marker_config = [];

    for (let i in data)
    {
        data[i];
        let icon_url="/static/img/yes.png";
        console.log(i);
        if (data[i]['status']=='inuse')
            icon_url="/static/img/no.png";

        marker_config.push(
            {
                position:{lng:parseFloat(data[i]['position'][0]),lat:parseFloat(data[i]['position'][1])},
                icon:{url:icon_url,scaledSize: new google.maps.Size(50, 50)},
                map: map,
                title: data[i]['_id']
            })
        info_config.push(
            '<h4>車位使用中</h4>' +
            '<h6>車位ID:'+data[i]['_id']+'</h6>' +
            '<a class="btn btn-danger" href="https://www.google.com.tw/maps/dir//'+parseFloat(data[i]['position'][1])+','+parseFloat(data[i]['position'][0])+'/@'+parseFloat(data[i]['position'][1])+','+parseFloat(data[i]['position'][0])+',16z/data=!4m2!4m1!3e0?hl=zh-TW">導航到該車位</a><br>' +
            '<span>上次更新時間： 00:00</span><br/>',
        )
    }
    console.log(marker_config)
    //設定 Info window 內容
    info_config.forEach(function (e, i) {
        infoWindows[i] = new google.maps.InfoWindow({
            content: e
        });
    });
    //標出 marker
    marker_config.forEach(function (e, i) {
        markers[i] = new google.maps.Marker(e);
        markers[i].setMap(map);
        markers[i].addListener('click', function () {
            infoWindows[i].open(map, markers[i]);
        });
    });
    function _geocoder(address) {
        geocoder.geocode({
            address: address
        }, function (results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                LatLng = results[0].geometry.location;
                return results;
            }
        });
    }
}