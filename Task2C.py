from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_highest_rel_level

def run():
    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
 
    print(stations_highest_rel_level(stations, 10)) 

    
run()
