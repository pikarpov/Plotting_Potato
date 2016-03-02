'''
Plotting Potato is here to plot:
    column data from a file in supported formats:
        .xlsx, .xls (data taken from first sheet by default)
        .csv, .txt, .dat (tab, comma, semicolon delimited)
    linear, semilog, log funcitons

To set filepath, a function, and edit various parameters of the graphs,
go to corresponding def:  PlotData or PlotFunction

By default, everything will be constructed on the same plot.

If you will try to change styles and want to revert to default,
make sure to re-run the code in a new console.

gl hf

-Platobob
'''

from pylab import *
from matplotlib import style
import matplotlib.pyplot as plt
from numpy import genfromtxt
import xlrd
import sys
import numpy as np
from scipy.stats import chisquare
from scipy.stats import linregress

def main():
    #size of the plot window
    figure(figsize=(10,6), dpi=80)

    '''
    #------Plot Style-----
    #xkcd-styled plots...try it, I dare you :P
    plt.xkcd()

    #additional ones5
    print style.available
    style.use('fivethirtyeight')
    '''

    #What do you want to plot?
    #Comment out whichever you don't need here
    PlotData()
    PlotFunction()

    #position of the legend, can be from 1 to 10
    plt.legend(loc=4)
    plt.grid(True)

    #figure x and y ranges are automatic unless specified
    #plt.xlim([0.0, 1.0])
    plt.tick_params(axis='x', labelsize=12)
    #plt.ylim([0.0, 6.0])
    plt.tick_params(axis='y', labelsize=12)
    plt.xlabel(r'Swag', fontsize=24)
    plt.ylabel(r'Baba', fontsize=24)
    plt.title(r'Cookie', fontsize=16)

    #save the figure using next line;  choose w/e format (ex: .png, .jpg, .eps)
    #plt.savefig('BlazeIt.png', format = 'png')

    plt.show()

def PlotData():
    #path to your data
    filename = r'data.xlsx'

    #Sheet number in case it is .xlsx file;  won't have any effect for .txt and such
    sheetnumb = 0

    values = ImportData(filename, sheetnumb)

    x = values[0]     #Column containing x-values
    y = values[1]     #Column containing y-values
    xerr = values[2]  #Column containing error values for x
    yerr = values[3]  #Column containing error values for y

    #plot the data; index of values[i] corresponds to column #, starting with 0
    plt.plot(x, y, marker = 'o', linestyle='None', label = 'Cookies')
    #determines the line of best fit as a first order polynomial
    coef = np.polyfit(x, y , 1)
    fit = np.poly1d(coef)
    print "Line of best fit:", fit
    x_space = np.linspace(-2.0, 2.0 ,1000)
    plt.plot(x_space, fit(x_space))

    #plot the errorbars

    plt.errorbar(x, y, xerr, yerr, linestyle="None", color='black')

    #find chi-squared in the slope
    expected = fit(values[1]) #takes the equation from the fit and calculates the expected values
                                    # from the x-values of your input
    print "Expected values from fit:", expected            #prints the expected value, make sure they make sense!!!
    print "Experimental values:", y
    chi_square = chisquare(y, expected, 1, None) #calculates chi-squared with experimental data
                                                            # third number is degrees of freedom
    print "Chi_Squared:", chi_square.statistic
    print "P-value :", chi_square.pvalue      #i hope you know what this does

    #calculate standard error in slope
    linregression = linregress(x,y)
    print "Standard Error:", linregression.stderr


def PlotFunction():
    #assing what values of x to use in form np.linspace(min,max,number of points to take)
    x = np.linspace(-2.1,0,100)

    y = abs(sin(3*x)) + 1

    plt.plot(x, y, color ='red', label = 'BoobEyes')

    #semilog scale
    #plt.semilogx(x, y,  linestyle='None', marker = 'o', label = 'cookie')

    #log scale
    #plt.loglog(x, y, basex=10, basey=10,  linestyle='-', marker = 'o', label = 'cookie')



#--------------No Need to Go beyond this point----------------------

def ImportData(filename, sheetnumb):
    global content
    global sheet
    values = []

    if filename.endswith('.xlsx') or filename.endswith('.xls'):
        content = xlrd.open_workbook(filename, 'r')

        sheet = content.sheet_by_index(sheetnumb)
        column = sheet.ncols
        row = sheet.nrows
        excel = True

    elif filename.endswith('.csv') or filename.endswith('.txt') or filename.endswith('.dat'):
        print r'Delimeter:  %r'% delimiter(filename)
        content = genfromtxt(filename, delimiter=delimiter(filename))
        column = len(content[0])
        row = len(content)
        excel = False

    else:
        sys.exit("Wtf, mate?")


    print '# of Columns: %d'% column
    print '# of Rows:    %d'% row

    for j in range(column):
        data = []
        counter = 0
        for i in range(0, row):

            try:
                data.append(float(point(i,j, excel)))
            except:
                if counter == 0:
                    print 'Column %d title:  %s'%(j,point(i,j, excel))
                    counter +=1
                else:
                    break

        values.append(data)
    return values

def delimiter(filename):
    with open(filename, 'r') as content:
        header=content.readline()
        if header.find(";")!=-1:
            return ";"
        if header.find(",")!=-1:
            return ","
        if header.find("\t")!=-1:
            return "\t"
    return "Could not detect column delimiter"

def point(i,j, excel):
    if excel:
        return sheet.cell(i,j).value
    else:
        return content[i,j]

if __name__ == '__main__':
   main()
