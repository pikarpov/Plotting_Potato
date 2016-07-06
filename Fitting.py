"""
This file is part of Plotting_Potato.
Polynimial and function fitting functions are located here.

-Platobob & Pat

"""

from Plotting_Potato import ImportData, func
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chisquare
from scipy.stats import linregress
from scipy.optimize import curve_fit
from sympy import *

def FitPoly(name,x,y,degree):
    print("----------- Begin FitPoly -----------")    
    #determines the line of best fit as a first order polynomial
    coef = np.polyfit(x, y , degree)
    fit = np.poly1d(coef)
    print("Line of best fit:", fit)
    x_space = np.linspace(min(x)-0.2*abs(min(x)),max(x)+0.2*abs(min(x)),1000)
    plt.plot(x_space, fit(x_space), label=name)

    #find chi-squared in the slope
    expected = fit(y) #takes the equation from the fit and calculates the expected values
                      # from the x-values of your input
    print("\n Expected values from fit:", expected)           #prints the expected value, make sure they make sense!!!
    print("\n Experimental values:", y)
    chi_square = chisquare(y, expected, 1, None) #calculates chi-squared with experimental data
                                                            # third number is degrees of freedom
    print("\n Chi_Squared:", chi_square.statistic)
    print("\n P-value :", chi_square.pvalue)      #i hope you know what this does

    #calculate standard error in slope
    linregression = linregress(x,y)
    print("\n Standard Error:", linregression.stderr)
    print("----------- End FitPoly -----------\n")    

def FitFunction(name, x, y, a, **par):
#def FitFunction(x, y):
    print("----------- Begin FitFunction -----------")
      
    # Desired fit Function
    #def func(x,a,b,c):
    #    return a*np.exp(-((x-b)**2)/(4*c**2))

    # Range of x-axis and number of points within range
    x_space = np.linspace(min(x)-0.2*abs(min(x)),max(x)+0.2*abs(min(x)),1000)
    
    p0=[]
    p0.append(a)
    for key in par:
        p0.append(par[key])

    popt, pcov = curve_fit(func,x,y,p0)

    # popt - optimal values for parmaters so that the
    #  sum of the square error is minimized'
    # The order here is [a,b,c] as in func(x,a,b,c)
    print("Optimal values for parameters,")
    print("  minimizing the sum of the square error:")
    print(popt)

    # pcov - estimated covariance of popt.
    print("\n Covariance matrix for the fit:")
    print(pcov)

    # perr - standard deviation errors on the parameters
    # Evaluated from the square root of the covariance diagonal
    # The order here is again [a,b,c] as in func(x,a,b,c)
    print("\n Standard deviations for the fit parameters: ")
    perr = np.sqrt(np.diag(pcov))
    print(perr)

    # Plots the fit to your provided function
    plt.plot(x_space, func(x_space, *popt), label=name)

    print("----------- End FitFunction -----------\n")
