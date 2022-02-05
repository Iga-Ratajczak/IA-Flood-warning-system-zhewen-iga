
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    """Requirements for Task 1A"""

    # Build list of stations
    stations = build_station_list()
    x=0
    print(stations_by_distance(stations,x))
if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
