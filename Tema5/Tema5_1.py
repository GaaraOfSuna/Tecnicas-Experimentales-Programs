# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 19:24:46 2015

@author: GAARA
"""

import numpy as np
from matplotlib import pyplot as plt
from numpy.random import uniform, normal
import time

start_time = time.time()



def x(N):
    return np.random.uniform(0, 1, N)
    
def media(x, N, start):
    x_med=np.zeros(N-start)
    for i in np.arange(start, N):
        x_med[i-start]=1/(i+1)*sum(x(i))
    return x_med

def repet(n_2, rept):
    return np.random.uniform(0, 1, n_2*rept).reshape(rept, n_2).sum(axis=1)/n_2

N=1000.
n_2=1000
rept=10000

print np.mean(media(x, N, 0))
print np.std(media(x, N, 100))

plt.figure(1)
plt.subplot(121)
plt.axis([0, 100, 0.3, 0.7])
plt.plot(np.arange(0, N), media(x, N, 0), '-')

plt.subplot(122)
plt.axis([100, 1000, 0.3, 0.7])
plt.plot(np.arange(100, N), media(x, N, 100), '-')

print np.mean(media(x, N, 0))
print np.std(media(x, N, 100))

plt.figure(2)
plt.subplot(121)
plt.axis([0.3, 0.7, 0, 30])
plt.hist(media(x, N, 0), bins=30, normed=True)

plt.subplot(122)
plt.axis([0.3, 0.7, 0, 30])
plt.hist(media(x, N, 100), bins=30, normed=True)

print np.mean(repet(n_2, rept))
print np.std(repet(n_2, rept))

plt.figure(3)
plt.subplot(111)
plt.axis([0, 1, 0, 60])
plt.hist(repet(n_2, rept), bins=20, normed=True)

print ("--- %s seconds ---" % (time.time() - start_time))
plt.draw()
plt.show()