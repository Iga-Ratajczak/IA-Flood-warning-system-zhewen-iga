
from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_by_distance
from haversine import haversine, Unit

def test_stations_by_distance():
    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s_list=list(s)
    cambridge = (52.2053, 0.1218) # (lat, lon)
    temp=stations_by_distance(s_list, cambridge)
    assert round(temp,4)==6038