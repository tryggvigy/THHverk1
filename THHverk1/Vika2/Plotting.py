'''
Created on 5.2.2014

@author: Notandi
'''
import matplotlib.pyplot as plt
import numpy as np

def plot(y, timi):
    x = np.arange(0,timi,1)
    plt.plot(x,y)
    plt.show()