# -*- coding: utf-8 -*-
"""
Created on Fri Nov 06 11:52:49 2015
@author: GAARA
"""

import numpy as np
from matplotlib import pyplot as plt


def y(x):
    return 1/((np.sin(x/2))**4)
    
print y(np.pi/9)/5
print y(np.pi/9/2*3)/5
print y(np.pi/9/2*4)/5
print y(np.pi/9/2*5)/5
print y(np.pi/9/2*6)/5
print y(np.pi/9/2*7)/5
print y(np.pi/9/2*8)/5
print y(np.pi/9/2*9)/5
print y(np.pi/9/2*12)/5

x=np.linspace(np.pi/4, np.pi, 1000)   
plt.figure()
plt.subplot(111)
plt.plot(x, y(x)*5, '-')

plt.draw()
plt.show()