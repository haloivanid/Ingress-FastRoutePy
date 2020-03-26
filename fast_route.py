import requests
import json
import time
import gpxpy
import threading
import datetime
import re

API_TOKEN = '5b3ce3597851110001cf6248c3fff330345849a4971e71d32c695c77'

class GPScalc:
	def __init__(self, data):
		self.gps = data
		self.gps_calc = []
		self.data_calc = []

	def check_list(self):
		if len(self.gps_calc) == 0:
			return self.gps
		else:
			return [x for x in self.gps if x not in self.gps_calc]

	def range_data(self):
		return self.range

def bookmark():
	guid = []
	returnData = []
	with open('bookmark.txt', 'r') as d:
		data_json = json.loads(d.read())
		for i in data_json['portals']['idOthers']['bkmrk']:
			guid.append(data_json['portals']
				['idOthers']['bkmrk'][i])
		for x in guid:
			pid = x['guid']
			label = x['label']
			lat = float(x['latlng'].split(',')[0])
			lng = float(x['latlng'].split(',')[1])
			returnData.append([label, [lat, lng], pid])
	return returnData

def calc_data():
	n_data = len(bookmark())
	possibility = int((n_data*(n_data-1))/2)
	start = datetime.datetime.now()
	time_run_rec = []
	route = []
	gCalc = GPScalc(bookmark())
	while True:
		for i in gCalc.check_list():
			for x in range(len(gCalc.check_list())):
				if gCalc.check_list()[x] != i:
					time_run_rec.append(1)
					# print(f'{i[0]}\tto\t{gCalc.check_list()[x][0]}')
					print(f'Collecting route data: {len(time_run_rec)}/{possibility}')
					print(f'{i[1]}\tto\t{gCalc.check_list()[x][1]}')
					xy1 = xy1=i[1]
					xy2 = gCalc.check_list()[x][1]
					data = get_route_distance(xy1, xy2)
					if len(time_run_rec)%40 == 0:
						if not len(gCalc.check_list()) == 2:
							end = datetime.datetime.now()
							if end-start < datetime.timedelta(seconds=60):
								while True:
									work_time = str(datetime.datetime.now()-start).split('.')[0]
									if str(work_time) == str(datetime.timedelta(seconds=61)):
										break
							else:
								while True:
									work_time = str(datetime.datetime.now()-start).split('.')[0]
									sync_work_time = re.sub(r'.*:', '0:00:', work_time)
									if str(sync_work_time) == str(datetime.timedelta(seconds=58)):
										time.sleep(3)
										break
							start = datetime.datetime.now()
					gCalc.data_calc.append([i[2], gCalc.check_list()[x][2], data])
			gCalc.gps_calc.append(i)
		break

	poi_calc = {}
	for i in bookmark():
		item = []
		for x in gCalc.data_calc:
			if i[2] == x[0]:
				item.append([i[2], x[1], x[2]])
			elif i[2] == x[1]:
				item.append([i[2], x[0], x[2]])
		poi_calc[item[0][0]] = item

	guid = list(poi_calc.keys())
	nGUID = []
	def check_guid():
		if len(nGUID) == 0:
			return guid
		else:
			return [x for x in guid if x not in nGUID]

	nCheck = [check_guid()[0]]
	while True:
		if not len(check_guid()) == 1:
			min_range = []
			for x in poi_calc[nCheck[0]]:
				min_range.append(x[2])
			min_r = min_range.index(min(min_range))

			POI = poi_calc[nCheck[0]][min_r][0]
			nPOI = poi_calc[nCheck[0]][min_r][1]

			for i in check_guid():
				for p in poi_calc[i]:
					if POI in p:
						poi_calc[i].remove(p)

			nCheck.append(nPOI)
			del poi_calc[nCheck[0]]
			nCheck.remove(POI)
			nGUID.append(POI)

			route.append(POI)
		else:
			route.append(nPOI)
			break

	return route


def get_route_distance(xy1, xy2):
	while True:
		try:
			body = {"coordinates":[[xy1[1],xy1[0]],[xy2[1],xy2[0]]]}
			headers = {
				'Accept': 'application/json, application/geo+json, '
				'application/gpx+xml, img/png; charset=utf-8',
				'Authorization': API_TOKEN,
				'Content-Type': 'application/json; charset=utf-8'
			}
			url = 'https://api.openrouteservice.org/v2/directions/cycling-road'
			call = requests.post(url, json=body, headers=headers)
			data = json.loads(call.text)
			returnData = float(data['routes'][0]['summary']['distance'])
			return returnData
			break
		except Exception as e:
			print('JSON DATA ERROR: retrying to connect...')
			time.sleep(2)


def route2gpx(list_xy):
	if not len(list_xy) > 1:
		raise ValueError('need more coordinates')
	else:
		yx = []
		for i in list_xy:
			rev_coor = [i[1], i[0]]
			yx.append(rev_coor)

			body = {"coordinates":yx, "elevation":"true"}
			headers = {
				'Accept': 'application/json, application/geo+json, '
				'application/gpx+xml, img/png; charset=utf-8',
				'Authorization': API_TOKEN,
				'Content-Type': 'application/json; charset=utf-8'
			}
			url = 'https://api.openrouteservice.org/v2/directions/cycling-road/gpx'
			call = requests.post(url, json=body, headers=headers)
			
		with open('route.gpx', 'w+') as f:
			gpx = gpxpy.parse(call.text)
			f.write(gpx.to_xml())


def process():
	route_gps = []
	for i in calc_data():
		for x in bookmark():
			if i == x[2]:
				route_gps.append(x[1])
	print('-'*25)
	print('Build the data...')
	route2gpx(route_gps)
	print('-'*25)
	return route_gps
