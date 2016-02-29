# -*- coding: utf-8 -*-
"""
Created on Sun Feb 07 12:14:33 2016

@author: GAARA
"""

import numpy as np
from matplotlib import pyplot as plt
from numpy.random import uniform, normal
import time

start_time = time.time()

def f(alpha, x):
    """propability distribution"""
    return 0.5*(1+alpha*x**2)
    
def F(alpha, x):
    """mother function"""
    return 0.5*x+1./6*alpha*x**3+0.5+1./6*alpha
    
def x_1(alpha, epsilon):
    return 2*epsilon-1-1./3*alpha
    
def x_2(alpha, epsilon):
    return (6*epsilon/alpha)**(1./3)

n=1000
epsilon=np.random.uniform(0, 1, n)
alpha=0.9

x=x_1(alpha, epsilon)+x_2(alpha, epsilon)
print np.mean(x)
plt.figure(1)
plt.subplot(111)
plt.plot(np.arange(0, 10), F(0.9, np.arange(10)), '-')
    
print ("--- %s seconds ---" % (time.time() - start_time))

plt.draw()
plt.show()

"""
f(x)=0.5+0.5*a*x**2

a_1=0.5 g_1=1           int(g_1)=2
a_2=0.5 g_2=a*x**2      int(g_2)=2/3*a

b_1=1           h_1=0.5
b_2=1/3*a       h_2=3/2*x**2

F_1=0.5*x
F_2=0.5*x**3
"""