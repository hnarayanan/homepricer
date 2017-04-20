var mymap = L.map('mapid').setView([51.505, -0.09], 13);
L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?access_token={accessToken}', {
    accessToken: 'pk.eyJ1IjoiaG5hcmF5YW5hbiIsImEiOiJjajFwaDF2enEwMDAxMnduejFzZjg1NnEyIn0.KlcHvt6sAtxBrVUflJLTpA'
}).addTo(mymap);
L.geoJson(wards).addTo(mymap);
