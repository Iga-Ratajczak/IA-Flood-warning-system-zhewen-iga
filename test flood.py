from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels

def run_over_threshold():
    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
 
    assert(type(stations_level_over_threshold(stations, 0.8))) == list

run_over_threshold()

def run_highest_tel_level():
    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
 
    assert(len(stations_highest_rel_level(stations, 20)) == 20)

    
run_highest_tel_level()
