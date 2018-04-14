# Estimating property prices in the U.K. with Gaussian Processes

This repository contains code that goes along with an upcoming blog
post on [my personal website][personal-website]. Together, they act as
a systematic look at a statistical model called [the Gaussian
Process][wiki-gaussian-process], and use it to estimate future
property prices in the U.K. The blog post covers the underlying
theory, and the code in this repository encompasses a (Django) web
application that helps load historical transaction information and a
Gaussian Process model (in TensorFlow) that predicts future
prices. The web application uses OpenStreetMap to visualise
historical pricing data and future predictions.

## Setup

### Fetch the source code and install requirements

- Todo: pip requirements
- TODO: npm requirements

### Fetch initial data from different sources

- TODO: Historical property transaction data
  - https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads
  - http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-complete.csv
- TODO: Postcode geocodes (National Statistics Postcode Lookup)
  - http://geoportal.statistics.gov.uk
  - https://ons.maps.arcgis.com/home/item.html?id=3163014b9574492ea67804a9d5728c48 (and click Download)
- TODO: Postcode geoshapes
  - Wards (December 2014) Generalised Clipped Boundaries in Great Britain
  - http://geoportal.statistics.gov.uk/datasets/73f28a6716d747caa32f52d9aa5e92a3_2
  - http://geoportal.statistics.gov.uk/datasets/73f28a6716d747caa32f52d9aa5e92a3_2.geojson


## Usage

TODO: Here is how you run the webapp, and here is an example of it
running in the wild.

## Copyright and license

Copyright (c) 2016–2017 [Harish Narayanan](https://harishnarayanan.org).

https://www.gnu.org/licenses/agpl-3.0.en.html

Get in touch with me if you wish to do anything proprietary with it
(without sharing your improvements back to the community).

[personal-website]: https://harishnarayanan.org
[wiki-gaussian-process]: https://en.wikipedia.org/wiki/Gaussian_process
