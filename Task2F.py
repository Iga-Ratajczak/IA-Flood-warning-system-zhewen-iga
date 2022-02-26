import datetime
import numpy as np
from pytest import skip
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_level_over_threshold



def run():
    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    dt = 2
    dates, levels = [], []
    #5 stations at which the current relative water level is greatest and for a time period extending back 2 days
    #stations at which the current relative water level is greatest and for a time period
    #show typical low or high

    #general - works
    #for station in stations:
        #dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        #plot_water_level_with_fit(station,dates,levels,4)
    
    list_of_tuples=[]
    list_of_tuples=stations_level_over_threshold(stations, 0.0)
    #print(list_of_tuples)
    names=[]
    for i in range(5):
        names.append(list_of_tuples[i][0])
        print(names)

        for station in stations:
            if station.name==names[i]:
                #data error
                if station.name=='Letcombe Bassett':
                    skip
                else:

                    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
                    #print(dates)
                    plot_water_level_with_fit(station,dates,levels,4)
            else:
                pass
        
    


if __name__ == "__main__":
    print("*** Task 2A: CUED Part IA Flood Warning System ***")
    run()