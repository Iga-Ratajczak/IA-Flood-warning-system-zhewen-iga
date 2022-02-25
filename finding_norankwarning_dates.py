from floodsystem.analysis import polyfit
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import datetime 
import numpy as np
from dateutil.tz import tzutc
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
def run():

    stations = build_station_list()
    dt = 2
    dates, levels = [], []

    for station in stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        polyfit(dates,levels,4)


if __name__ == "__main__":
    print("*** Task 2A: CUED Part IA Flood Warning System ***")
    run()
