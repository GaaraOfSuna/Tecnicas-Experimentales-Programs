# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 11:00:58 2016

@author: GAARA
"""

import numpy as np
from scipy.stats.stats import pearsonr
from numpy.random import uniform, normal
from matplotlib import pyplot as plt
#from sympy import *

n=1000

x_1=np.random.uniform(0, 15, n)
x_3=np.random.uniform(25, 75, n)
y_1=np.random.uniform(0, 15, n)
y_3=np.random.uniform(0, 100, n)


x = 0
"""
x_1, x_3, y_1, y_3 = symbols('x_1 x_3 y_1 y_3')
f = 10000*((-sin(x)*(x_3-x_1)+100*cos(x))**2/((x_3-x_1)**2+(y_3-y_1)**2+10000)**3)
#print Integral(f, (x_1, 0, 15)).evalf()


var('y z')
c = y**(-y)+z
print Integral(c, (y, 0, 1), (z, 0, 1)).doit()

"""
def f(x, x_1, x_3, y_1, y_3):
    f = 10000*((-np.sin(x)*(x_3-x_1)+100*np.cos(x))**2/((x_3-x_1)**2+(y_3-y_1)**2+10000)**(3./2))
    return f

p=10
z=[]
for i in np.arange(p):
    z.append(np.mean(f(i*10*np.pi/180, x_1, x_3, y_1, y_3)))

print z   
fit=1.15*z[0]*np.cos((np.arange(p)*(10)+20)*np.pi/180)**2
#print f(x, x_1, x_3, y_1, y_3)
print np.mean(f(0, x_1, x_3, y_1, y_3))
print np.mean(f(10*np.pi/180, x_1, x_3, y_1, y_3))
print np.mean(f(20*np.pi/180, x_1, x_3, y_1, y_3))
print np.mean(f(30*np.pi/180, x_1, x_3, y_1, y_3))
print np.mean(f(50*np.pi/180, x_1, x_3, y_1, y_3))
print np.mean(f(60*np.pi/180, x_1, x_3, y_1, y_3))
print np.mean(f(80*np.pi/180, x_1, x_3, y_1, y_3))
print np.mean(f(90*np.pi/180, x_1, x_3, y_1, y_3))
print "###################"
print pearsonr(z, fit)[0]
print z[0]*1.15


plt.figure(1)
plt.subplot(111)
plt.plot(np.arange(p), z, '-')
plt.plot(np.arange(p), fit, '-')
    

plt.draw()
plt.show()

"""
1.15*cos²(alpha+20)
"""


