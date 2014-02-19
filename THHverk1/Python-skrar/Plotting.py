'''
Created on 5.2.2014

@author: Notandi
'''
import matplotlib.pyplot as plt
import numpy as np


def plot(data, label, xlabel, ylabel):
    x = np.arange(0,len(data),1)
    temp = plt.plot(x,data, c=np.random.rand(3,1), label = label)
    plt.legend(temp)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    return temp


def showPLot(myPlot):
    plt.show(myPlot)

def plotNafn(x1,y,xlabel,ylabel):
    x = np.arange(0,x1+1,1)
    plt.plot(x,y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


