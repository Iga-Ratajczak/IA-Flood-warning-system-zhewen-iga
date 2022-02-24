import datetime
import numpy as np
from floodsystem.stationdata import build_station_list
from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit



def run():
    # Build list of stations
    stations = build_station_list()
    dt = 2
    dates, levels = [], []
    #5 stations at which the current relative water level is greatest and for a time period extending back 2 days
    #stations at which the current relative water level is greatest and for a time period
    #show typical low or high

    for station in stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_level_with_fit(station,dates,levels,4)
    
    #for i in range(5):
    #   station_name,number=stations_level_over_threshold(stations, tol=0)
    #   names.append(station_name)
    #   for station in stations:
            #if station.name==names[i]:
            #   dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
            #   plot_water_level_with_fit(station,dates,levels,4)
            #else:
                #pass
        
    


if __name__ == "__main__":
    print("*** Task 2A: CUED Part IA Flood Warning System ***")
    run()