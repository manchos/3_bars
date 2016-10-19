import json
import os
from math import sin, cos, sqrt, atan2, radians


def load_data(filepath):
    """Return the list of bars."""
    if not os.path.exists(filepath):
        return None
    with open(filepath, encoding='utf8') as file_handler:
        return json.load(file_handler)


def get_biggest_bar(bars):
    """Return the biggest bar from the list of bars."""
    # big_bar = bars[0]
    # for bar in bars:
    #     if bar['Cells']['SeatsCount'] > big_bar['Cells']['SeatsCount']:
    #         big_bar = bar
    # return big_bar['Cells']['Name']
    return max(bars, key=lambda x: x['Cells']['SeatsCount'])['Cells']['Name']


def get_smallest_bar(bars):
    """Return the smallest bar from the list of bars."""
    # small_bar = bars[0]
    # for bar in bars:
    #     if bar['Cells']['SeatsCount'] < small_bar['Cells']['SeatsCount']:
    #         small_bar = bar
    # return small_bar['Cells']['Name']
    return min(bars, key=lambda x: x['Cells']['SeatsCount'])['Cells']['Name']


def get_closest_bar(data, lon1, lat1):
    """Return the closest bar from the list of bars given the GPS coordinates."""
    closest_bar = data[0]
    distance_min = distance(lon1, lat1, closest_bar['Cells']['geoData']['coordinates'][0],
                            closest_bar['Cells']['geoData']['coordinates'][1])
    for bar in data:
        distance_cur = distance(lon1, lat1, bar['Cells']['geoData']['coordinates'][0],
                                bar['Cells']['geoData']['coordinates'][1])
        if distance_min > distance_cur:
            distance_min = distance_cur
            closest_bar = bar
    return closest_bar['Cells']['Name']



def distance(lon1, lat1, lon2, lat2):
    """Return the distance between the points"""
    earth_radius = 6373.0
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    return earth_radius * 2 * atan2(sqrt(a), sqrt(1 - a))


if __name__ == '__main__':
    filepath = input('Enter the real path to json file with list of bars:')
    bars = load_data(filepath)
    print('----------------------------------------------------')
    print('The biggest bar: %s' % get_biggest_bar(bars))
    print('The smallest bar: %s' % get_smallest_bar(bars))
    print('----------------------------------------------------')
    lon1 = float(input('Enter the longitude:'))
    lat1 = float(input('Enter the latitude:'))
    # 37.439787, 55.85051  # metro station Skhodnenskaya
    print('the closest bar near the metro station Skhodnenskaya: %s' % get_closest_bar(bars, lon1, lat1))
