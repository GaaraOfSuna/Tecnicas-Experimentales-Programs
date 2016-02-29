# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 22:23:47 2015

@author: GAARA
"""
import numpy as np
from sympy import *
from numpy.random import uniform, normal
from matplotlib import pyplot as plt

def R(a, b, c, d, e, k):
    """The function R"""    
    return  a/(((b-c)*d/(k*e))-2*a*(1-k*d/e))

def differentiation(R):
    A, B, C, D, E, K = symbols('A B C D E K')
    p_1 = []    
    p_2 = [A, B, C, D, E, K]
    for i in np.arange(len(p_2)):
        p_1.append(R(A, B, C, D, E, K).diff(p_2[i]))
    return p_1

def error(differentiation, a, b, c, d, e, k, sigma_a, sigma_b, sigma_c, sigma_d, sigma_e, sigma_k):
    A, B, C, D, E, K = symbols('A B C D E K')
    dR = 0
    p_sigma = [sigma_a, sigma_b, sigma_c, sigma_d, sigma_e, sigma_k]
    for i in np.arange(len(p_sigma)):
        dR += (differentiation(R)[i].subs([(A, a), (B, b), (C, c), (D, d), (E, e), (K, k)])*p_sigma[i])**2
    return dR

def error2(differentiation, a, b, c, d, e, k, sigma_a, sigma_b, sigma_c, sigma_d, sigma_e, sigma_k):
    A, B, C, D, E, K = symbols('A B C D E K')
    dR = 0
    p_sigma = [sigma_a, sigma_b, sigma_c, sigma_d, sigma_e, sigma_k]
    for i in np.arange(len(p_sigma)):
        dR += (differentiation(R)[i].subs([(A, a), (B, b), (C, c), (D, d), (E, e), (K, k)])*p_sigma[i])
    return dR
    
def count(gauss):
    """Returns the amount of items in gau that return true from condition"""
    i = 0
    for x in gauss:
        if x>0.42:
            i+=1
    return i
#Main
a = 3.84
b = 74
c = 9.5
d = 0.112
e = 0.32
k = 0.89

sigma_a = 1.33
sigma_b = 4.
sigma_c = 3.
sigma_d = 0.009
sigma_e = 0.02
sigma_k = 0

N=10000.

a_ran = np.random.normal(a, sigma_a, N)
b_ran = np.random.normal(b, sigma_b, N)
c_ran = np.random.normal(c, sigma_c, N)
d_ran = np.random.normal(d, sigma_d, N)
e_ran = np.random.normal(e, sigma_e, N)

print "a) R =", R(a, b, c, d, e, k)
print "El error es:", sqrt(error(differentiation, a, b, c, d, e, k, sigma_a, sigma_b, sigma_c, sigma_d, sigma_e, sigma_k))
print "b)", (1-0.975835)*100, "%"
print "c) Mean=", np.mean(R(a_ran, b_ran, c_ran, d_ran, e_ran, k)), "Std=", np.std(R(a_ran, b_ran, c_ran, d_ran, e_ran, k))
print "d) Porcentaje es:", count(R(a_ran, b_ran, c_ran, d_ran, e_ran, k))/N*100, "%"
print "e) Porcentaje es:", count(R(a, b_ran, c, d_ran, e_ran, k))/N*100, "%"
print "El error es:", sqrt(error(differentiation, a, b, c, d, e, k, 0, sigma_b, 0, sigma_d, sigma_e, sigma_k))
print "Mean=", np.mean(R(a, b_ran, c, d_ran, e_ran, k)), "Std=", np.std(R(a, b_ran, c, d_ran, e_ran, k))


plt.figure(1)
plt.subplot(111)
plt.axis([0, 1, 0, 14])
plt.hist(R(a_ran, b_ran, c_ran, d_ran, e_ran, k), bins=100, label='datos', normed=True)

plt.figure(2)
plt.subplot(111)
plt.axis([0, 1, 0, 14])
plt.hist(R(a, b_ran, c, d_ran, e_ran, k), bins=100, label='datos', normed=True)

plt.draw()
plt.show()