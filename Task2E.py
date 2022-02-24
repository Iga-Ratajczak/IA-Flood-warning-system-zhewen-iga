import matplotlib.dates as mdates
import datetime
import numpy as np
from floodsystem.stationdata import build_station_list
from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels

from floodsystem.plot import plot_water_levels


def run():
    # Build list of stations
    stations = build_station_list()
    dt = 10
    dates, levels = [], []
    #5 stations at which the current relative water level is greatest and for a time period extending back 2 days
    #stations at which the current relative water level is greatest and for a time period
    #show typical low or high

    #for i in range(5):
    #   station_name,number=stations_level_over_threshold(stations, tol=0)
    #   names.append(station_name)
    #   for station in stations:
            #if station.name==names[i]:
            #   dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
            #   plot_water_level_with_fit(station,dates,levels,4)
            #else:
                #pass
    #t = [(2016, 12, 30), (2016, 12, 31), (2017, 1, 1),(2017, 1, 2), (2017, 1, 3), (2017, 1, 4),(2017, 1, 5)]
    #x = mdates.date2num(t)
    #print(x)
    for station in stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        print(dates)
        plot_water_levels(station,dates,levels)

    


if __name__ == "__main__":
    print("*** Task 2A: CUED Part IA Flood Warning System ***")
    run()