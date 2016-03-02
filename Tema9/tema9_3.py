# -*- coding: utf-8 -*-
"""
Created on Wed Mar 02 18:19:45 2016

@author: GAARA
"""

import numpy as np
from numpy.random import exponential, normal, randn
from matplotlib import pyplot as plt
from scipy.optimize import leastsq

def func(x, A, B, mu, sigma, tau):
    return A/np.sqrt(2*np.pi*sigma**2)*np.exp(-(x-mu)**2/2/sigma**2)+B/tau*np.exp(-x/tau)


n=10000
A=1/3.
B=2/3.
s = np.random.normal(5, 0.25, n)
b = np.random.exponential(3, n)

f = A*s+B*b

Adat, Bdat, Cdat, Ddat, Edat  = 1/3., 2/3., 5, 0.25, 3
xdat = np.linspace(1.45, 18.8, n)
y_true=np.sort(func(xdat, Adat, Bdat, Cdat, Ddat, Edat))
y_meas = func(np.sort(f), Adat, Bdat, Cdat, Ddat, Edat)

def residuals(p, y, x):
    A, B, mu, sigma, tau = p
    err = y - A/np.sqrt(2*np.pi*sigma**2)*np.exp(-(x-mu)**2/sigma**2)+B/tau*np.exp(-x/tau)
    return err
    
def peval(x, p):
    return p[0]/np.sqrt(2*np.pi*p[2]**2)*np.exp(-(x-p[1])**2/p[2]**2)+p[4]/p[3]*np.exp(-x/p[3])

p0 = [2/4., 5.5, 0.3, 2.5, 2/4.]
np.array(p0)

plsq = leastsq(residuals, p0, args=(y_meas, xdat))

print plsq[0]

print y_true
print f

plt.figure(1)
plt.subplot(121)
plt.xlim([0, 10])
plt.xlabel('f')
plt.hist(f, bins=150)

plt.subplot(122)
plt.plot(xdat, np.sort(y_true))
plt.plot(xdat, np.sort(f))

plt.draw()
plt.show()