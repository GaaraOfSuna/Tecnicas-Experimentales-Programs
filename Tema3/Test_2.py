# -*- coding: utf-8 -*-
"""
Created on Wed Dec 09 19:12:29 2015

@author: GAARA
"""

from sympy import *

def R(a, x):
    return a*x**2 + 1
    
x, a = symbols('x a')
xprime = R(a, x).diff(x)
aprime = R(a, x).diff(a)
    
print xprime.subs(a, 2)