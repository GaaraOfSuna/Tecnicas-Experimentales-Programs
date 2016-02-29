# -*- coding: utf-8 -*-
"""
Created on Wed Oct 07 12:08:23 2015

@author: GAARA
"""

from numpy import *
from matplotlib import pyplot as plt
from numpy.random import uniform, normal
from scipy.stats.stats import pearsonr


N     = 10000                                     # Zahl der Elemente
num   = arange(0, N)                              # Array zur Nummerierung
x_1   = uniform(0, 1, N)
x_1_b = uniform(-1, 1, N)
x_2   = uniform(0, 1, N)
mw    = x_1**2
mw_b  = x_1_b**2         
sigma = 0.1
gauss = normal(mw, sigma)                         # Gaußsche Normalverteilung

print pearsonr(x_1+x_2, x_2)[0]                   # Routine zur Koeffizienten-
print pearsonr(gauss, x_1)[0]                     # berechnung
print pearsonr(normal(mw_b, sigma), x_1_b)[0]
print pearsonr(0.99, 3)[0]

# Berechnung von Hand
# V_ij=mean((gauss-mean(gauss))*(x_2-mean(x_2)))
# V_ii=mean((gauss-mean(gauss))*(gauss-mean(gauss)))
# V_jj=mean((x_2-mean(x_2))*(x_2-mean(x_2)))
# coeff=V_ij/(sqrt(V_ii*V_jj))
# print coeff
   
# Erstellen des Diagramms
plt.figure(1, figsize=(15, 7))                                    
plt.subplot(231)       
plt.xlabel("x_1")
plt.ylabel("x_2")
plt.plot(x_1, x_2, linestyle='none', marker='.', ms=1)

plt.subplot(232)      
plt.xlabel("x_1")
plt.ylabel("Gauss")
plt.plot(x_1, gauss, linestyle='none', marker='.', ms=1)

plt.subplot(233)      
plt.xlabel("x_1")
plt.ylabel("Normal")
plt.plot(x_1_b, normal(mw_b, sigma), linestyle='none', marker='.', ms=1)

plt.subplot(234)
plt.hist(x_1, bins=100, normed=True)

plt.subplot(235)
plt.hist(gauss, bins=100, normed=True)

plt.subplot(236)
plt.hist(normal(mw_b, sigma), bins=100, normed=True)

#plt.figure(2, figsize=(10, 5))                                    
#plt.subplot(121)
#plt.title("Histograma")
#plt.xlabel("numeros aleatorios")
#plt.ylabel("x_1")
#plt.plot(num, x_1, linestyle='none', marker='.', ms=1)
                                    
#plt.subplot(122)
#plt.title("Histograma_2")
#plt.ylabel("x_1")
#plt.hist(x_1, bins=100, normed=True)

plt.draw()
plt.show()