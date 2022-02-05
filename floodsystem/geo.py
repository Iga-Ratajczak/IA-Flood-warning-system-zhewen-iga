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

#task 1B
def stations_by_distance(stations, p):
    print(type(p))
    
    #test if p is called,
    assert type(p)==tuple
    assert len(p)==2
    list_with_distance=[]

    #test if stations are called
    #test if sorted
    for station in stations:
        #temporary_tuple=()
        distance=haversine(station.coord, p)
        temporary_tuple=(station.name, station.town, distance)
        list_with_distance.append(temporary_tuple)
    list_with_distance = sorted_by_key(list_with_distance,2)
    
    return list_with_distance
        #lyon = (45.7597, 4.8422) # (lat, lon)
        #print(haversine(station.coord,p))

#task 1D

#part 1

#part2
def stations_by_river(stations):
    #check stations called correctly
    station_by_river = {}
    for station in stations:
        river=station.river
        if  river in station_by_river:
            station_by_river[station.river].append(station.name)
            station_by_river[station.river].sort() 
        else:
            station_by_river[station.river]=[station.name]           
    return station_by_river
#task 1E
def rivers_by_station_number(stations, N):
    river_list=[]
    dict_of_stations_river=stations_by_river(stations)
    
    for station in stations:
        river=station.river
        if  river in dict_of_stations_river:
            tupletemp=()
            #print(len(dict_of_stations_river[river]))
            tupletemp=(river, len(dict_of_stations_river[river]))

        river_list.append(tupletemp)
    river_list = sorted_by_key(river_list,1)
    #print(river_list)
    biggest=[]
    for i in range (N):
        biggest.append(river_list[i])
    return biggest