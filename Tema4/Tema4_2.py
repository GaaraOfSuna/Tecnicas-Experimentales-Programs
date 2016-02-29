# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 22:07:09 2015

@author: GAARA
"""

from numpy import *
from matplotlib import pyplot as plt
from numpy.random import uniform, normal, chisquare
from scipy import special as sp
from scipy import stats as st
from scipy import integrate


def chiqua(gauss, mu, sigma):
    """Definition of the value of chi-squared"""
    return sum(((gauss-mu)/sigma)**2)

def distribucion(chiqua, mu, sigma, n, N):
    """repetition of the experiment 10000 times"""
    arr = arange(N)
    empty = zeros(N)
    for i in arr:
        gau = random.normal(130, sigma, n)
        empty[i]=chiqua(gau, mu, sigma)
    return empty
    
def f(x, n):
    """calculation of chi-squared"""
    return ((exp(-x/2))*x**((n/2)-1))/((2**(n/2))*sp.gamma(n/2))

def Prob(chi, n):
    """return probability that X**2> definit limit"""
    # return 1-integrate.quad(lambda x: f(x, n), 0, alpha)[0]
    return st.chi2.sf(chi, n)    
    
# Main
N  = 10000                      # number of repetitions
n  = 10.                         # degrees of freedome
mu = 130                        # mean
sigma = sqrt(n)                 # mean derivation
x_arr = linspace(0, 50, 1000, endpoint=False)   # an array
chi = chisquare(n, N)           # Random distribution chi-squared

#Draw function
plt.figure(1, figsize=[15, 8])                                    
#plt.subplot(111)
#plt.hist(chi, bins=300, label='datos', normed=True)
#plt.plot(x_arr, f(x_arr, n), '-', color='r', label='funciona chi-quadrado')
#plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)


plt.subplot(111)
plt.axis([0, 50, 0, 0.16])
plt.hist(distribucion(chiqua, mu, sigma, n, N), bins=100, label='datos', normed=True)
plt.plot(x_arr, f(x_arr, n), '-', color='r', label='funciona chi-quadrado')
#plt.plot(x_arr, f(x_arr, n*3.5), '-', color='y', label='nueva aproximacion de funciona chi-quadrado')
plt.legend(loc=1)


#plt.subplot(122)
#plt.axis([0, 1, 0, 3])
#plt.hist(Prob(distribucion(chiqua, mu, sigma, n, N), n), bins=100, label='probabilidad de chi-quadrado', normed=True)
#plt.plot(x_arr/50, ones(1000), '-', color='r', label='funciona uniforme')
#plt.legend(loc=1)


plt.draw()
plt.show()