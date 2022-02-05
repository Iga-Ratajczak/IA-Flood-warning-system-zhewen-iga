
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river

def run():
    """Requirements for Task 1D"""
    

    # Build list of stations
    stations = build_station_list()
    x=stations_by_river(stations)
    
    print("stations next to river aire")
    print( x["River Aire"])
    print("stations next to river cam")
    print(x["River Cam"])
    print("stations next to river thames")
    print(x["River Thames"])


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    
    run()
