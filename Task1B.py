
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from haversine import haversine, Unit

def run():
    """Requirements for Task 1B"""
    

    # Build list of stations
    stations = build_station_list()
    cambridge = (52.2053, 0.1218) # (lat, lon)
    temp=stations_by_distance(stations, cambridge)
    print("Ten closest")
    print (temp[:10])
    print("ten furthest")
    print (temp[-10:])

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    
    run()