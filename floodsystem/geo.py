# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from math import dist
from os import stat
from .utils import sorted_by_key  # noqa
from .station import MonitoringStation
from floodsystem.stationdata import build_station_list
from haversine import haversine, Unit
#stations 
#p - tuple

#calculates the distance between given coordinate p and the location of the station


def stations_by_distance(stations, p):
    list_with_distance=[]

    for station in stations:
        temporary_tuple=()
        distance=haversine(station.coord, p)
        temporary_tuple=(station.name, station.town, distance)
        list_with_distance.append(temporary_tuple)
    return list_with_distance
        #lyon = (45.7597, 4.8422) # (lat, lon)
        #print(haversine(station.coord,p))
     

