# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 16:07:56 2016

@author: GAARA
"""


import numpy as np
from numpy.random import uniform
from matplotlib import pyplot as plt
import time

start_time = time.time()

def dec(xi, tau):
    """decay funcion"""
    return 1/tau*np.exp(-xi/tau)  
    
def x(xi, tau):
    """the function function"""
    return -tau*np.log(1-xi)
    
def x_sigma(n, x, tau_tilde):
    """calculatest sigma_tilde"""
    return 1./n*sum((x-tau_tilde)**2)

def y(tau, x):
    """Monte-Carlo-Simulation"""
    y=[]
    for i in np.arange(10000):
        xi=np.random.uniform(0, 1, n)
        y.append(np.mean(-tau*np.log(1-xi)))
    return y   

def L(x, tau, n):
    """definition of the likelihood-function"""
    return 1/tau**n * np.exp(-x/tau)

def x_max(L, rand):
    """calculate x-value of the global maximum"""
    return rand[np.argmax(L)]

def FWHM(X,Y):
    half_max = max(Y) / 2.
    #find when function crosses line half_max (when sign of diff flips)
    #take the 'derivative' of signum(half_max - Y[])
    d = np.sign(half_max - np.array(Y[0:-1])) - np.sign(half_max - np.array(Y[1:]))
    #plot(X,d) #if you are interested
    #find the left and right most indexes
    left_idx = np.argmax(d)
    right_idx = np.argmin(d)
    return X[right_idx] - X[left_idx] #return the difference (full width)

#Datos
n=50
tau=1
xi=np.random.uniform(0, 1, n)
x=x(xi, tau)
rand=np.linspace(0.5, 2, 50)            # Data for x-axis
L=L(sum(x), rand, n)
tau_tilde=np.mean(x)

# Output    
print tau_tilde
print np.var(x)
  
"""
L(xi, tau)=prod((1-xi)/tau)

L(xi, tau)=1/tau**n * np.exp(sum(x)/tau)
"""

print x_max(L, rand)
print np.sqrt(FWHM(rand, L))

plt.figure(1)
plt.subplot(121)
plt.hist(y(tau, x), bins=100)

plt.subplot(122)
plt.plot(rand, L, '-')

print ("--- %s seconds ---" % (time.time() - start_time))

plt.draw()
plt.show()