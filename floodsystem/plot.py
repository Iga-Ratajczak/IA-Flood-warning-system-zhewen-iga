import numpy as np
from floodsystem.analysis import polyfit

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
#To handle warnings as errors simply use this:
import warnings
warnings.filterwarnings("error")

def plot_water_levels(station, dates, levels):
    if station.typical_range != None:
        low = station.typical_range[0]
        high = station.typical_range[1]
        print ("low : ",low)
        if low < high:
            x = mdates.date2num(dates)
            y = levels
            plt.plot(x, y, '.')
            plt.xlabel("time")
            plt.ylabel("water level")
            plt.title(station.name)
            plt.axhline(y=low, color='b', linestyle='-')
            plt.axhline(y=high, color='r', linestyle='-')
            plt.show()
        else:
            pass
        
    return None

def plot_water_level_with_fit(station, dates, levels, p):
    x = mdates.date2num(dates)
    y = levels
    low = station.typical_range[0]
    high = station.typical_range[1]
    poly, offset=polyfit(dates,levels,p)
    if offset==0:
        # Plot original data points
        plt.plot(x, y, '.')
        plt.xlabel("time")
        plt.ylabel("water level")
        plt.title(station.name)

        # Plot polynomial fit at 30 points along interval
        x1 = np.linspace(x[0], x[-1], 30)
        plt.plot(x1, poly(x1))

        #typical range
        plt.axhline(y=low, color='b', linestyle='-')
        plt.axhline(y=high, color='r', linestyle='-')

        # Display plot
        plt.show()
    else:
        print("here")

        # Plot original data points
        plt.plot(x, y, '.')
        plt.xlabel("time")
        plt.ylabel("water level")
        plt.title(station.name)

        # Plot polynomial fit at 30 points along interval (note that polynomial
        # is evaluated using the shift x)
        #unsure if is should linspace it
        x1 = np.linspace(x[0], x[-1], 30)
        plt.plot(x1, poly(x1 - x[0]))

        #typical range
        plt.axhline(y=low, color='b', linestyle='-')
        plt.axhline(y=high, color='r', linestyle='-')

        # Display plot
        plt.show() 
    
    return None
    