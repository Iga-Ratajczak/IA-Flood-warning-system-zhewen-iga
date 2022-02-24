
from floodsystem.analysis import polyfit
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import datetime 
import numpy as np
from dateutil.tz import tzutc
import warnings
warnings.filterwarnings("error")

def test_polyfit():
    y = [0.1, 0.09, 0.23, 0.34, -0.05]
    dates=[datetime.datetime(2022, 2, 23, 21, 15, tzinfo=tzutc()), datetime.datetime(2022, 2, 23, 21, 0, tzinfo=tzutc()), datetime.datetime(2022, 2, 23, 20, 45, tzinfo=tzutc()), datetime.datetime(2022, 2, 23, 20, 30, tzinfo=tzutc()), datetime.datetime(2022, 2, 23, 20, 15, tzinfo=tzutc())]
    x_converted=mdates.date2num(dates)

    # Using shifted x values, find coefficient of best-fit
    # polynomial f(x) of degree 4
    p_coeff = np.polyfit(x_converted - x_converted[0], y, 4)

    # Convert coefficient into a polynomial that can be evaluated
    # e.g. poly(0.3)
    
    poly = np.poly1d(p_coeff)
    offset=x_converted[0]

    poly_tested,offset_tested=polyfit(dates,y,4)
    #checks that it givesthe warning and sets an offset
    #makes sure that the right type is returned
    print(poly)
    print(poly_tested)
    #assert round(poly)==round(poly_tested)
    
    assert offset==offset_tested
    assert poly==poly_tested
    return offset_tested