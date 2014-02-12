'''
Created on 5.2.2014

@author: Notandi
'''
import matplotlib.pyplot as plt
import numpy as np
g_doPlot = True

def plot(y, timi):
    x = np.arange(0,timi,1)
    plt.plot(x,y)
    plt.show()

def plotNafn(x1,y,xlabel,ylabel):
    x = np.arange(0,x1+1,1)
    plt.plot(x,y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()