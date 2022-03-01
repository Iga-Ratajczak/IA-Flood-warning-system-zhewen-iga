from binascii import Incomplete
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import flood_risk
import datetime


def run():
    stations = build_station_list()
    update_water_levels(stations)
    dt = 1
    dates, levels = [], []
    extremely_severe = []
    severe=[]
    high=[]
    moderate=[]
    low=[]
    incomplete = []
    count = 0
    for station in stations:
        count += 1

        try:
            dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
            risk = flood_risk(station, dates, levels, 4)
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
        except:
            incomplete.append(station.name)


        if count>200:
                break

    print('stations with extremely severe risk:{}'.format(extremely_severe))
    print('stations with severe risk:{}'.format(severe))
    print('stations with high risk:{}'.format(high))
    print('stations with moderate risk:{}'.format(moderate))
    print('stations with low risk:{}'.format(low))
    print('stations with incomplete data:{}'.format(incomplete))

run()
