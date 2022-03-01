from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.station import MonitoringStation

    # Create a station - river x
s_id = "test-s-id"
m_id = "test-m-id"
label = "some station"
coord = (-2.0, 4.0)
trange = (-2.3, 3.4445)
river = "River X"
town = "My Town"
s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
s.latest_level = 3.1

    # Create a station2 - river x2
s_id = "test-s-id2"
m_id = "test-m-id2"
label = "some station2"
coord = (-3.0, 5.0)
trange = (-2.4, 6.4445)
river = "River X2"
town = "My Town"
s2= MonitoringStation(s_id, m_id, label, coord, trange, river, town)
s2.latest_level = 6.8

    # Create a station3 - river x
s_id = "test-s-id3"
m_id = "test-m-id3"
label = "some station3"
coord = (-3.0, 5.0)
trange = (-2.4, 6.4445)
river = "River X"
town = "My Town"
s3= MonitoringStation(s_id, m_id, label, coord, trange, river, town)
s3.latest_level = 6.3

    # Create a station4 - river x2
s_id = "test-s-id4"
m_id = "test-m-id4"
label = "some station4"
coord = (-3.0, 5.0)
trange = (-2.4, 6.4445)
river = "River X2"
town = "My Town"
s4= MonitoringStation(s_id, m_id, label, coord, trange, river, town)
s4.latest_level = 5.5

    # Create a station5 - river y
s_id = "test-s-id5"
m_id = "test-m-id5"
label = "some station5"
coord = (-3.0, 5.0)
trange = (-2.4, 6.4445)
river = "River Y"
town = "My Town"
s5= MonitoringStation(s_id, m_id, label, coord, trange, river, town)
s5.latest_level = 4.3

stations=[]
stations.append(s)
stations.append(s2)
stations.append(s3)
stations.append(s4)
stations.append(s5)
def run_over_threshold():
    # Build list of stations

 
   assert(stations_level_over_threshold(stations, 0.8) == [('some station2', 1.0401944711402566), ('some station3', 0.9836621629261122), ('some station', 0.9400295935242405), ('some station4', 0.8932104697834813)])

run_over_threshold()

def run_highest_tel_level():
    # Build list of stations
 
    assert(stations_highest_rel_level(stations, 3) == [('some station2', 1.0401944711402566), ('some station3', 0.9836621629261122), ('some station', 0.9400295935242405)])

    
run_highest_tel_level()
