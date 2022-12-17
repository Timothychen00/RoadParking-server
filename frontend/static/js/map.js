function initMap() {
    var markers = [];
    var infoWindows = [];
    //設定中心點
    var map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: 25.04, lng: 121.512 },
        zoom: 14
    });
    var geocoder = new google.maps.Geocoder();
    console.log(geocoder);

    //info windows
    var info_config = [

        '<h4>車位使用中</h4>' +
        '<a class="btn btn-danger" href="https://google.com">導航到該車位</a><br>' +
        '<span>上次更新時間： 00:00</span><br/>',

        '<h4>車位無人使用</h4>' +
        '<a class="btn btn-success" href="https://google.com">導航到該車位</a><br>' +
        '<span>上次更新時間： 00:00</span><br/>',
    ];

    //建立地圖 marker 的集合
    var marker_config = [{
        position: { lat: 25.035, lng: 121.519 },
        icon:
        {
            url: "static/img/no.png",
            scaledSize: new google.maps.Size(50, 50)
        },
        map: map,
        title: '車位1'
    }, {
        position: { lat: 25.033, lng: 121.519 },
        icon:
        {
            url: "static/img/yes.png",
            scaledSize: new google.maps.Size(50, 50)
        },
        map: map,
        title: '車位2'
    }];
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