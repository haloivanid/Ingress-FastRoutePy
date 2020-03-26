import folium
import gpxpy
import fast_route
import time

def overlayGPX(coordinates, zoom):
	gpx_file = open('route.gpx', 'r')
	gpx = gpxpy.parse(gpx_file)
	points = []
	for route in gpx.routes:
		for point in route.points:
			points.append([point.latitude, point.longitude])

	lat = sum(p[0] for p in points)/len(points)
	lon = sum(p[1] for p in points)/len(points)

	mymap = folium.Map(location=[lat,lon], zoom_start=zoom)
	
	folium.PolyLine(points, color="red", weight=4, opacity=0.5).add_to(mymap)
	
	for r in points:
		folium.Circle([r[0], r[1]],
			radius=0.5,
			color="red",
			opacity=1,
			fill_color="red",
			fill_opacity=1
			).add_to(mymap)
	
	for e, c in enumerate(coordinates):
		folium.Circle([c[0], c[1]],
			radius=5,
			color="blue",
			fill_color="cyan",
			opacity=1,
			fill_opacity=1,
			popup=f'Dest no. {e+1}'
			).add_to(mymap)

	for c in coordinates:
		folium.Circle([c[0], c[1]],
			radius=40,
			color="gold",
			opacity=1,
			).add_to(mymap)

	mymap.save('index.html')

def main():
	n_data = len(fast_route.bookmark())
	possibility = int((n_data*(n_data-1))/2)

	print(f'You will go to {n_data} POI')
	print('-'*25)
	time.sleep(0.5)
	print(f'We have {possibility} possible route')
	print('-'*25)
	time.sleep(0.5)
	print('Calculating and arrange the best route for you')
	print('-'*25)
	overlayGPX(fast_route.process(), 15)
	print("Your route has been finished")
	print("Let's open index.html file")

if __name__ == '__main__':
	main()