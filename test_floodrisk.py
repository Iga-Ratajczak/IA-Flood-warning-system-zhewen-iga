from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import flood_risk
from floodsystem.station import MonitoringStation

import datetime 
from dateutil.tz import tzutc
import numpy as np
from floodsystem.analysis import polyfit

def test_floodrisk():

        # Create a station - river x
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (0.5, 1.5)
    river = "River X"
    town = "My Town"

    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town,)
    s.latest_level=1.45

    levels=[1.495, 1.498, 1.508, 1.514, 1.514, 1.523, 1.531, 1.535, 1.536, 1.543, 1.554, 1.556, 1.56, 1.569, 1.576, 1.567, 1.575, 1.573, 1.582, 1.583, 1.576, 1.587, 1.571, 1.572, 1.56, 1.553, 1.549, 1.523, 1.513, 1.498, 1.487, 1.476, 1.455, 1.435, 1.424, 1.413, 1.399, 1.387, 1.379, 1.364, 1.36, 1.35, 1.346, 1.34, 1.338, 1.339, 1.329, 1.317, 1.312, 1.306, 1.298, 1.29, 1.277, 1.27, 1.264, 1.253, 1.243, 1.236, 1.227, 1.216, 1.207, 1.199, 1.192, 1.185, 1.179, 1.172, 1.171, 1.164, 1.16, 1.162, 1.157, 1.15, 1.147, 1.143, 1.137, 1.138, 1.134, 1.132, 1.129, 1.126, 1.132, 1.128, 1.125, 1.128, 1.128, 1.129, 1.125, 1.126, 1.129]
    dates=[datetime.datetime(2022, 3, 1, 13, 45, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 13, 30, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 13, 15, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 13, 0, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 12, 45, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 12, 30, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 12, 15, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 12, 0, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 11, 45, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 11, 30, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 11, 15, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 11, 0, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 10, 45, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 10, 30, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 10, 15, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 10, 0, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 9, 45, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 9, 30, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 9, 15, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 9, 0, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 8, 45, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 8, 30, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 8, 15, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 8, 0, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 7, 45, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 7, 30, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 7, 15, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 7, 0, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 6, 45, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 6, 30, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 6, 15, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 6, 0, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 5, 45, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 5, 30, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 5, 15, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 5, 0, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 4, 45, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 4, 30, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 4, 15, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 4, 0, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 3, 45, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 3, 30, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 3, 15, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 3, 0, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 2, 45, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 2, 30, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 2, 15, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 2, 0, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 1, 45, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 1, 30, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 1, 15, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 1, 0, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 0, 45, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 0, 30, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 0, 15, tzinfo=tzutc()), datetime.datetime(2022, 3, 1, 0, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 23, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 23, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 23, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 23, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 22, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 22, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 22, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 22, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 21, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 21, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 21, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 21, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 20, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 20, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 20, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 20, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 19, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 19, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 19, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 19, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 18, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 18, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 18, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 18, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 17, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 17, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 17, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 17, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 16, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 16, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 16, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 16, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 28, 15, 45, tzinfo=tzutc())]

        #chosen values for relative water level such that risk=3, gradient negative
    risk_predicted="High"

    risk_assessed=flood_risk(s,dates,levels,4)
    print(risk_assessed)
    assert risk_assessed==risk_predicted

    #grad = (poly(x1[49])-offset)-(poly(x1[0])-offset)
    #print(grad)

    #derivative=np.polyder(poly)
    #print(x[-1])
    #grad=derivative(x[-1])
    #grad2=(poly(x[-1])-poly(x[0]))/(x[-1]-x[0])
    #print(grad)
    #print(grad2)

    #16000928383584.0