from .station import MonitoringStation
from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    selected = []

    for station in stations:
        if station.relative_water_level() != None and station.typical_range_consistent() == True: 
            if station.relative_water_level() > tol:
                selected.append(tuple((station.name, station.relative_water_level())))
        selected.sort(key=lambda y: y[1], reverse=True)

    return selected

def stations_highest_rel_level(stations, N):
    selected = []

    for station in stations:
        if station.relative_water_level() != None: 
            selected.append(tuple((station.name, station.relative_water_level())))
        selected.sort(key=lambda y: y[1], reverse=True)

    return selected[0: N]


    