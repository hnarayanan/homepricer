function getColor(w) {
    return prices[w] > 2000000 ? '#800026' :
           prices[w] > 1000000 ? '#BD0026' :
           prices[w] > 500000  ? '#E31A1C' :
           prices[w] > 250000  ? '#FC4E2A' :
           prices[w] > 100000  ? '#FD8D3C' :
           prices[w] > 50000   ? '#FEB24C' :
           prices[w] > 25000   ? '#FED976' :
                                 '#FFEDA0';
}

function style(feature) {
    return {
        fillColor: getColor(feature.properties.wd16cd),
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
