function getColor() {
    // TODO: This function currently returns a random colour from a
    // set. It needs to return the actual average property price in
    // the enclosing shape.
    var colors = ['#800026', '#BD0026', '#E31A1C', '#FC4E2A', '#FD8D3C', '#FEB24C', '#FED976', '#FFEDA0'];
    // var colors = ['#0c2c84', '#225ea8', '#1d91c0', '#41b6c4', '#7fcdbb', '#c7e9b4', '#edf8b1', '#ffffd9'];
    return colors[Math.floor(Math.random() * colors.length)];
}

function style(feature) {
    return {
        fillColor: getColor(),
        weight: 0.5,
        opacity: 0.5,
        color: '#800026',
        fillOpacity: 0.7
    };
}

var map = L.map('map').setView([51.505, -0.09], 13);
L.tileLayer(
    'https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?access_token={accessToken}', {
	accessToken: 'pk.eyJ1IjoiaG5hcmF5YW5hbiIsImEiOiJjajFwaDF2enEwMDAxMnduejFzZjg1NnEyIn0.KlcHvt6sAtxBrVUflJLTpA'
    }
).addTo(map);
L.geoJson(regions, {style: style}).addTo(map);
