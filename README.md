# Ingress-FastRoutePy
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-green.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![built with Python3](https://img.shields.io/badge/built%20with-Python3-blue.svg)](https://www.python.org/)
[![openrouteservice API](https://img.shields.io/badge/openrouteservice-API-red.svg)](https://openrouteservice.org/)

This project will calculate the best route from Ingress Portal selection for you, using fast route mode in Open Route Service and will generate the "route.gpx" and "index.html" file.

## How to install Ingress-FastRoutePy
You will need Python3 (Tested using version 3.8 and 3.7) better if you build it using virtualenv
```sh
$ git clone https://github.com/haloivanid/Ingress-FastRoutePy.git
$ cd Ingress-FastRoutePy
$ pip install -r requirements.txt
```

## How to run Ingress-FastRoutePy
```sh
First, you must have some point of coordinates data from IITC and save into "bookmark.txt"
Second, you will need openrouteservice API (create account and get it free)
$ Open and edit "fast_route.py" file.
$ find API_TOKEN = 'Paste Your API Here' (in line 7)
$ save
You're ready to go
$ python main.py
```
