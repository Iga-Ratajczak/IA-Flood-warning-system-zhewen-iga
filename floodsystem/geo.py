# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
# from math import dist
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
    '''function sorts stations by distance from the chosen location (need to be input as coordinate)'''
    print(type(p))
    
    #test if p is called,
    assert type(p)==tuple
    assert len(p)==2
    list_with_distance=[]

    #test if stations are called
    
    for station in stations:
        distance=haversine(station.coord, p)
        temporary_tuple=(station.name, station.town, distance)
        list_with_distance.append(temporary_tuple)
    list_with_distance = sorted_by_key(list_with_distance,2)
    
    return list_with_distance

#task 1C
def stations_within_radius(stations, centre, r):
    list_of_stations = []
    for station in stations:
        distance = haversine(centre, station.coord)
        if distance <= r:
            list_of_stations.append(station.name)
        list_of_stations = sorted_by_key(list_of_stations, 0)
    return list_of_stations

#task 1D
#part 1
def rivers_with_station(stations):
    rivers_with_station = set()
    for station in stations:
        rivers_with_station.add(station.river)
    rivers_with_station = sorted_by_key(rivers_with_station, 0)
    return rivers_with_station

#part2
def stations_by_river(stations):
    '''combines stations that are connected to the same river as a list'''
    #test stations called correctly
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
    '''sorts rivers by the number of stations that are connected to it, in descending order'''
    river_list=[]
    dict_of_stations_river=stations_by_river(stations)
    #test stations called correctly
    river_list_no_rep={}

    for station in stations:
        river=station.river
        if  river in dict_of_stations_river:
            tupletemp=()
            tupletemp=(river, len(dict_of_stations_river[river]))
            if river in river_list_no_rep.keys():
                pass
            else:
                river_list_no_rep[river]=[0]
                river_list.append(tupletemp)
               

    #it sorts tuples in growing order by number of stations            
    river_list = sorted_by_key(river_list,1)
    #print(river_list)

    biggest=[]
    i=0
    for i in range (N):
        if len(river_list)-i-1>-1:
            biggest.append(river_list[len(river_list)-i-1])

    #when there are more rivers with the same number of stations as the N th entry, include these rivers in the list. 
    last_entry=river_list[len(river_list)-i-1]
    number=len(river_list)-i-2
    if number<0:
        pass
    else:
        next_potential_entry=river_list[len(river_list)-i-2]
        while last_entry[1]==next_potential_entry[1]:
                biggest.append(next_potential_entry)
                last_entry=next_potential_entry
                next_potential_entry=river_list[len(river_list)-i-3]
                i+=1

    return biggest