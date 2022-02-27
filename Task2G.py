from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import flood_risk
import datetime


def run():
    stations = build_station_list()
    update_water_levels(stations)
    extremely_severe = []
    severe=[]
    high=[]
    moderate=[]
    low=[]
    count = 0
    for station in stations:
        count += 1
        try:
            dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=1))
            risk = flood_risk(station, dates, levels, 4)
        except:
            risk = "Low"
        if risk == "Extremely Severe":
            extremely_severe.append(station.name)
        if risk == "Severe":
            severe.append(station.name)
        elif risk == "High":
            high.append(station.name)
        elif risk == "Moderate":
            moderate.append(station.name)
        elif risk == "Low":
            low.append(station.name)
        if count>200:
            break

    print(extremely_severe)
    print(severe)
    print(high)
    print(moderate)
    print(low)

run()
