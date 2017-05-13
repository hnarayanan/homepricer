import Leaflet from 'react-leaflet';
import React from 'react';
import { render } from 'react-dom';

import SimpleExample from './simple';

Leaflet.Icon.Default.imagePath = '//cdnjs.cloudflare.com/ajax/libs/leaflet/1.0.3/images/';

const examples = (
  <div>
    <h1>React-Leaflet examples</h1>
    <h2>Popup with Marker</h2>
    <SimpleExample />
  </div>
);

render(examples, document.getElementById('app'));
