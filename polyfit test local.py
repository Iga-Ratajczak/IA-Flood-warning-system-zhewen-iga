from floodsystem.analysis import polyfit
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import datetime 
import numpy as np
from dateutil.tz import tzutc
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
def run():


    y = [0.1, 0.09, 0.23, 0.34, -0.05]
    dates= [datetime.datetime(2022, 2, 25, 4, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 25, 3, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 25, 3, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 25, 3, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 25, 3, 0, tzinfo=tzutc())]

    x_converted=mdates.date2num(dates)

    # Using shifted x values, find coefficient of best-fit
    # polynomial f(x) of degree 4
    p_coeff = np.polyfit(x_converted, y, 4)

    # Convert coefficient into a polynomial that can be evaluated
    # e.g. poly(0.3)
    
    poly = np.poly1d(p_coeff)
    offset=0

    poly_tested,offset_tested=polyfit(dates,y,4)
    #checks that it givesthe warning and sets an offset
    #makes sure that the right type is returned
    print(poly)
    print(poly_tested)
    print(offset)
    print(offset_tested)
    assert poly==poly_tested
    assert offset==offset_tested
    assert poly==2

if __name__ == "__main__":
    print("*** Task 2A: CUED Part IA Flood Warning System ***")
    run()