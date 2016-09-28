import json
import os
from math import sin, cos, sqrt, atan2, radians


def load_data(filepath):
	if not os.path.exists(filepath):
		return None
	with open(filepath, encoding = 'utf8' ) as file_handler:
		return json.load(file_handler)




def get_biggest_bar(bars):
	big_bar = bars[0]
	for bar in bars:
		if bar['Cells']['SeatsCount'] > big_bar['Cells']['SeatsCount']:
			big_bar = bar
	return big_bar


def get_smallest_bar(bars):
	small_bar = bars[0]
	for bar in bars:
		if bar['Cells']['SeatsCount'] < small_bar['Cells']['SeatsCount']:
			small_bar = bar
	return small_bar


def get_closest_bar(data, lon1, lat1):
    closest_bar = data[0]
    distance_min = distance(lon1, lat1, closest_bar['Cells']['geoData']['coordinates'][0], closest_bar['Cells']['geoData']['coordinates'][1])
    for bar in data:
    	distance_cur = distance(lon1, lat1, bar['Cells']['geoData']['coordinates'][0], bar['Cells']['geoData']['coordinates'][1])
    	if distance_min > distance_cur:
    		distance_min = distance_cur
    		closest_bar  = bar
    return closest_bar     

def distance(lon1, lat1, lon2, lat2):
	earth_radius = 6373.0
	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2	
	return earth_radius * c * 2 * atan2(sqrt(a), sqrt(1 - a))


if __name__ == '__main__':
    filepath = 'E:\\python\\projects\\devmanorg\\3_bars\\Бары.json'
    data = load_data(filepath)
    print(data[0]['Cells']['Name'])
    print(get_biggest_bar(data))
    print(get_smallest_bar(data))
    lon1, lat1 = 37.439787, 55.85051 # метро Сходненская
    print(get_closest_bar(data, lon1, lat1))

