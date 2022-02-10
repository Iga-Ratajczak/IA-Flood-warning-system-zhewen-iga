from floodsystem.station import MonitoringStation
from floodsystem.geo import rivers_by_station_number

def test_stations_by_river():
    # Create a station - river x
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create a station2 - river x2
    s_id = "test-s-id2"
    m_id = "test-m-id2"
    label = "some station2"
    coord = (-3.0, 5.0)
    trange = (-2.4, 6.4445)
    river = "River X2"
    town = "My Town"
    s2= MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create a station3 - river x
    s_id = "test-s-id3"
    m_id = "test-m-id3"
    label = "some station3"
    coord = (-3.0, 5.0)
    trange = (-2.4, 6.4445)
    river = "River X"
    town = "My Town"
    s3= MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create a station4 - river x2
    s_id = "test-s-id4"
    m_id = "test-m-id4"
    label = "some station4"
    coord = (-3.0, 5.0)
    trange = (-2.4, 6.4445)
    river = "River X2"
    town = "My Town"
    s4= MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    

    # Create a station5 - river y
    s_id = "test-s-id5"
    m_id = "test-m-id5"
    label = "some station5"
    coord = (-3.0, 5.0)
    trange = (-2.4, 6.4445)
    river = "River Y"
    town = "My Town"
    s5= MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    stations=[s,s2,s3,s4,s5]
    

    #for more than one station with the same river
    x=rivers_by_station_number(stations,2)

    #checks that it calls all stations, checks the order of sorting
    y=rivers_by_station_number(stations,5)
    print(stations[1])

    assert x==[('River X2', 2), ('River X', 2)]
    assert y==[('River X2', 2), ('River X', 2), ('River Y', 1)]