from turtle import st
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run():
    """Requirements for Task 1E"""
    

    # Build list of stations
    stations = build_station_list()
    x=rivers_by_station_number(stations,9)
    
    print(x)


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IE Flood Warning System ***")
    
    run()
