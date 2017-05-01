function getColor(w) {
    return prices[w] > 1000000? '#d73027':
           prices[w] > 500000 ? '#fc8d59':
           prices[w] > 250000 ? '#fee08b':
           prices[w] > 200000 ? '#ffffbf':
           prices[w] > 150000 ? '#d9ef8b':
           prices[w] > 100000 ? '#91cf60':
           prices[w] > 50000  ? '#1a9850':
                                '#ffffff';
}

//Red--Green
// #d73027
// #fc8d59
// #fee08b
// #ffffbf
// #d9ef8b
// #91cf60
// #1a9850

// Red--Blue
// #b2182b
// #ef8a62
// #fddbc7
// #f7f7f7
// #d1e5f0
// #67a9cf
// #2166ac

// Red--Green--Blue
// #d53e4f
// #fc8d59
// #fee08b
// #ffffbf
// #e6f598
// #99d594
// #3288bd
// #ffffff

function style(feature) {
    return {
        fillColor: getColor(feature.properties.wd16cd),
        weight: 0.5,
        opacity: 0.5,
        color: '#333333',
        fillOpacity: 0.7
    };
}

var map = L.map('map').setView([51.505, -0.09], 10);
L.tileLayer(
    'https://api.mapbox.com/styles/v1/mapbox/bright-v9/tiles/256/{z}/{x}/{y}?access_token={accessToken}', {
	accessToken: 'pk.eyJ1IjoiaG5hcmF5YW5hbiIsImEiOiJjajFwaDF2enEwMDAxMnduejFzZjg1NnEyIn0.KlcHvt6sAtxBrVUflJLTpA',
	detectRetina: true
    }
).addTo(map);
L.geoJson(regions, {style: style}).addTo(map);


// setInterval(function(){
//     setTimeout(function(){
// //	L.geoJson(regions, {style: style}).addTo(map);
//     }, 2000);
// }, 4000);
