from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_with_station
def test_stations_within_radius():
    stations = build_station_list()
    for station in stations:
        assert stations_within_radius(stations, (52.2053, 0.1218), 10) is not None

def test_rivers_with_station():
    stations = build_station_list()
    for station in stations:
        assert rivers_with_station(stations) is not None
