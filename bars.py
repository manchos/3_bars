import json
import os
from math import sin, cos, sqrt, atan2, radians


def load_data(filepath):
	if os.path.exists(filepath):
		with open(filepath, encoding = 'utf8' ) as data_file:
			data = json.load(data_file)
			return data
	else:
		return 'file not found'




def get_biggest_bar(data):
	m = data[0]
	for i in data:
		if i['Cells']['SeatsCount'] > m['Cells']['SeatsCount']:
			m = i
	return m


def get_smallest_bar(data):
	m = data[0]
	for i in data:
		if i['Cells']['SeatsCount'] < m['Cells']['SeatsCount']:
			m = i
	return m


def get_closest_bar(data, lon1, lat1):
    cl = data[0]
    distance_min = distance(lon1, lat1, cl['Cells']['geoData']['coordinates'][0], cl['Cells']['geoData']['coordinates'][1])
    for i in data:
    	distance_cur = distance(lon1, lat1, i['Cells']['geoData']['coordinates'][0], i['Cells']['geoData']['coordinates'][1])
    	if distance_min > distance_cur:
    		distance_min = distance_cur
    		#print(distance_min)
    		#print(i['Cells']['Name'])
    		cl = i
    return cl    

def distance(lon1, lat1, lon2, lat2):
	R = 6373.0
	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))
	return R * c


if __name__ == '__main__':
    filepath = 'E:\\python\\projects\\devmanorg\\3_bars\\Бары.json'
    data = load_data(filepath)
    print(data[0]['Cells']['Name'])
    print(get_biggest_bar(data))
    print(get_smallest_bar(data))
    lon1, lat1 = 37.439787, 55.85051 # метро Сходненская
    print(get_closest_bar(data, lon1, lat1))

