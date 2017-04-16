# Estimating property prices in the U.K. with Gaussian Processes

This repository contains code that goes along with an upcoming blog
post on [my personal website][personal-website]. Together, they act as
a systematic look at a statistical model called [the Gaussian
Process][wiki-gaussian-process], and use it to estimate future
property prices in the U.K. The blog covers the underlying theory, and
the code in this repository encompasses a web application (in Django)
that helps load historical transaction information, visualise it
(using D3) and predicts future prices using a Gaussian Process model
in TensorFlow.

## Setup

### Fetch the source code and install requirements

- TODO: pip requirements
- TODO: npm requirements

### Fetch initial data from different sources

- TODO: Historical property transaction data
  - https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads
- TODO: Postcode geocodes
  - http://geoportal.statistics.gov.uk
  - http://ons.maps.arcgis.com/home/item.html?id=a26683d2393743f4b87c89141cd1b2e8
- TODO: Postcode geoshapes


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
