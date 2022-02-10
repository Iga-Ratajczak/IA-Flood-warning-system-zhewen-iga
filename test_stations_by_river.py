from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_by_river

def test_stations_by_river():
    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s_list=[]
    s_list.append(s)
    x=stations_by_river(s_list)

    assert x[river]==[label]