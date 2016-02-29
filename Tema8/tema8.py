# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 15:26:41 2016

@author: GAARA
"""


from iminuit import Minuit
import numpy as np
from numpy.random import uniform, normal
from matplotlib import pyplot as plt


def f(x, a, b, x_max, x_min):
    """the function"""
    return np.log((1+a*x+b/3*x**2)/(x_max-x_min+0.5*a*(x_max**2-x_min**2)+b/3*(x_max**3-x_min**3)))

 
# Main
a=0.5
b=0.5
x_min=-0.95
x_max=0.95

N=2000
x=np.sort(np.random.uniform(x_min, x_max, N))

alpha= np.random.normal(0.508, 0.052, 500)
beta= np.random.normal(0.47, 0.11, 500)

def L(x, a, b):
    return sum(x/(1+a*x+b*x**2))

#m = Minuit(f, x=P, fix_x=True, limit_x=(-1,1), a=0.5, error_a=0.01, b=0.5, error_b=0.01, x_min=-0.95, x_max=0.95, fix_x_min=True, fix_x_max=True)
#m.migrad()
#m.draw_mnprofile('a')
   
#print 'covariance', m.covariance
#print(m.values)
#print(m.errors)

plt.figure(1)
plt.subplot(111)
plt.xlabel('f(x=[-0.95, 0.95], a = 0.5, b = 0.5)')
plt.ylabel('n/f')
#plt.xlim([-0.95, 0.95])
plt.hist(f(x, a, b, x_max, x_min), bins=100)

plt.figure(2)
plt.subplot(121)
plt.xlabel(r'$\alpha$')
plt.hist(alpha, bins=50)

plt.subplot(122)
plt.xlabel(r'$\beta$')
plt.hist(beta, bins=50)

plt.figure(3)
plt.subplot(111)
plt.plot(alpha, beta)

plt.draw()
plt.show()
