
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
#To handle warnings as errors simply use this:
import warnings
warnings.filterwarnings("error")


def polyfit(dates, levels, p):
    """Given the water level time history (dates, levels) for a station the function computes a least-squares fit of a polynomial of degree p to water level data. 
    It return a tuple of (i) the polynomial object and (ii) any shift of the time (date)"""
    
    try:

        # Create set of 10 data points on interval (0, 2)
        
        x = mdates.date2num(dates)
        y = levels

        # Find coefficients of best-fit polynomial f(x) of degree p
        p_coeff = np.polyfit(x, y, p)

        # Convert coefficient into a polynomial that can be evaluated,
        # e.g. poly(0.3)
        poly = np.poly1d(p_coeff)

        # Plot original data points
        #plt.plot(x, y, '.')

        # Plot polynomial fit at 30 points along interval
        #x1 = np.linspace(x[0], x[-1], 30)
        #plt.plot(x1, poly(x1))

        # Display plot
        #plt.show()
        #converting dates to floats
        offset=0
    except np.RankWarning:
        print("here")
        x = mdates.date2num(dates)
        y = levels

        # Find coefficients of best-fit polynomial f(x) of degree p with offset x[0]
        p_coeff = np.polyfit(x - x[0], y, p)
        offset=x[0]

        # Convert coefficient into a polynomial that can be evaluated,
        # e.g. poly(0.3)
        poly = np.poly1d(p_coeff)

        # Plot original data points
        #plt.plot(x, y, '.')

        # Plot polynomial fit at 30 points along interval (note that polynomial
        # is evaluated using the shift x)
        #unsure if is should linspace it
        #x1 = np.linspace(x[0], x[-1], 30)
        #plt.plot(x1, poly(x1 - x[0]))

        # Display plot
        #plt.show() 
    temptuple=(poly, offset)
    return temptuple
    