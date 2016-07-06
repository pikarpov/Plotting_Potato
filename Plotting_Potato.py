'''
Plotting Potato is here to plot:
    column data from a file in supported formats:
        .xlsx, .xls (data taken from first sheet by default)
        .csv, .txt, .dat (tab, comma, semicolon delimited)
    linear, semilog, log funcitons

-To set filepath see PlotData()
-To set fit function see func()
-To edit various parameters of the graphs,
refer to main() or to a corresponding def:
[PlotData or PlotFunction or FitFunction or FitPoly] 

By default, everything will be constructed on the same plot.

If you will try to change styles and want to revert to default,
make sure to re-run the code in a new console.

gl hf

-Platobob
'''

from matplotlib import style
import matplotlib.pyplot as plt
import numpy as np
from Fitting import *
from ImportData import *

def main():
    #size of the plot window
    plt.figure(figsize=(10,6), dpi=80)

    '''
    #------Plot Style-----
    #xkcd-styled plots...try it, I dare you :P
    plt.xkcd()

    #additional ones
    print style.available
    style.use('fivethirtyeight')
    '''
    #---------------------
    #What do you want to plot?
    #Comment out whichever you don't need here

    x, y = PlotData('Cookies')   #plots the data; go to the function to indicta filename
    
    #FitPoly('PolyFit',x,y,2)      #fits a polynomial [change the last parameter to the degree order]

    #FitFunction('FuncFit',x, y, a=0, b=0, c=0)       #lsqrfit a func() [edit below], must provide initial guess
    
    PlotFunction('JokerEyes')
    #---------------------
    
    #position of the legend, can be from 1 to 10
    plt.legend(loc=4)
    plt.grid(True)

    #figure x and y ranges are automatic unless specified
    #plt.xlim([0.0, 1.0])
    plt.tick_params(axis='x', labelsize=12)
    #plt.ylim([0.0, 6.0])
    plt.tick_params(axis='y', labelsize=12)
    plt.xlabel(r'Swag', fontsize=18)
    plt.ylabel(r'Baba', fontsize=18)
    plt.title(r'Yolo', fontsize=22)

    #save the figure using next line;  choose w/e format (ex: .png, .jpg, .eps)
    #plt.savefig('BlazeIt.png', format = 'png')

    plt.show()


# Desired fit Function
def func(x,a,b,c):
    return a*x**2+b*x+c


def PlotData(name):
    print("----------- Begin PlotData -----------")
    
    #path to your data
    filename = r'data1.xlsx'     
    
    #Sheet number in case it is .xlsx file;  won't have any effect for .txt and such
    sheetnumb = 0

    values = ImportData(filename, sheetnumb)

    x = values[0]     #Column containing x-values
    y = values[1]     #Column containing y-values
    #xerr = values[2]  #Column containing error values for x
    #yerr = values[3]  #Column containing error values for y

    #plot the data; index of values[i] corresponds to column #, starting with 0
    #set linestyle="None" if want to see the data points only
    plt.plot(x, y, marker = 'o', linestyle='-', label = name)

    #plot the errorbars
    #plt.errorbar(x, y, yerr, xerr, linestyle="None", color='black')

    print("----------- End PlotData ----------- \n")
    
    return x,y


def PlotFunction(name):
    #assing what values of x to use in form np.linspace(min,max,number of points to take)
    x = np.linspace(-1,1,100)

    y = abs(np.sin(3*x))/4
           
    plt.plot(x, y, label = name)

    #semilog scale
    #plt.semilogx(x, y,  linestyle='None', marker = 'o', label = 'cookie')

    #log scale
    #plt.loglog(x, y, basex=10, basey=10,  linestyle='-', marker = 'o', label = 'cookie')


if __name__ == '__main__':
   main()
