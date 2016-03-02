# -*- coding: utf-8 -*-
"""
Created on Wed Mar 02 12:39:10 2016

@author: GAARA
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy.stats.stats import pearsonr
from scipy.special import gamma

def distchi(x, n):
    return np.power(x, n/2-1)*np.exp(-x/2)/np.power(2, n/2)/gamma(n)
    
xdata = [-0.9, -0.7, -0.5, -0.3, -0.1, 0.1, 0.3, 0.5, 0.7, 0.9]
ydata = [81, 50, 35, 27, 26, 60, 106, 189, 318, 520]

coefficients_0 = np.polyfit(xdata, ydata, 0)
polynomial_0 = np.poly1d(coefficients_0)
ys_0 = polynomial_0(xdata)
chi2_0=sum((ydata-ys_0)**2/ys_0)

coefficients_1 = np.polyfit(xdata, ydata, 1)
polynomial_1 = np.poly1d(coefficients_1)
ys_1 = polynomial_1(xdata)
chi2_1=sum((ydata-ys_1)**2/ys_1)

coefficients_2 = np.polyfit(xdata, ydata, 2)
polynomial_2 = np.poly1d(coefficients_2)
ys_2 = polynomial_2(xdata)
chi2_2=sum((ydata-ys_2)**2/ys_2)

coefficients_3 = np.polyfit(xdata, ydata, 3)
polynomial_3 = np.poly1d(coefficients_3)
ys_3 = polynomial_3(xdata)
chi2_3=sum((ydata-ys_3)**2/ys_3)

coefficients_4 = np.polyfit(xdata, ydata, 4)
polynomial_4 = np.poly1d(coefficients_4)
ys_4 = polynomial_4(xdata)
chi2_4=sum((ydata-ys_4)**2/ys_4)

coefficients_5 = np.polyfit(xdata, ydata, 5)
polynomial_5 = np.poly1d(coefficients_5)
ys_5 = polynomial_5(xdata)
chi2_5=sum((ydata-ys_5)**2/ys_5)

print coefficients_1
print coefficients_2
print coefficients_3
print chi2_2
print chi2_3
print chi2_4
print chi2_5
print 'n', 10-5-1
print distchi(chi2_2, 7)
print distchi(chi2_3, 6)
print distchi(chi2_4, 5)
print distchi(chi2_5, 4)


plt.plot(xdata, ydata, 'o')
plt.plot(xdata, ys_0, label='r=0')
plt.plot(xdata, ys_1, label='r=1')
plt.plot(xdata, ys_2, label='r=2')
plt.plot(xdata, ys_3, label='r=3')
plt.plot(xdata, ys_4, label='r=4')
plt.plot(xdata, ys_5, label='r=5')
plt.ylabel('y')
plt.xlabel('x')
plt.xlim(-1,1)
plt.ylim(0,530)
plt.legend(loc=2)
plt.show()
    
