# Ingress-FastRoutePy
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-green.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![built with Python3](https://img.shields.io/badge/built%20with-Python3-blue.svg)](https://www.python.org/)
[![openrouteservice API](https://img.shields.io/badge/openrouteservice-API-red.svg)](https://openrouteservice.org/)

This project will calculate the best route from Ingress Portal selection for you, using fast route mode in Open Route Service and will generate the "route.gpx" and "index.html" file.

## How to install Ingress-FastRoutePy
> You will need Python3 (Tested using version 3.8 and 3.7) better if you build it using virtualenv
```sh
$ git clone https://github.com/haloivanid/Ingress-FastRoutePy.git
$ cd Ingress-FastRoutePy
$ pip install -r requirements.txt
```

## Prepare before run Ingress-FastRoutePy
1. You must have some point of coordinates data from IITC and save into "bookmark.txt"
2. Second, you will need openrouteservice API (create account and get it free) [Here](https://openrouteservice.org/dev/#/signup)
3. Open and edit "fast_route.py" file.
4. Find API_TOKEN = 'Paste Your API Here' (in line 7)
5. Save the file
6. You're ready to go

## How to run Ingress-FastRoutePy
```sh
$ python main.py
```
