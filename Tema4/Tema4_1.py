# -*- coding: utf-8 -*-
"""
Created on Wed Nov 04 23:58:48 2015

@author: GAARA
"""

from numpy import *
from matplotlib import pyplot as plt
from numpy.random import uniform, normal
from scipy.stats.stats import pearsonr

N    = 100000.0
mu_1 = 3
mu_2 = 3
sigma_1 = 2
sigma_2 = 0.5
theta   = -pi/6

gauss_1 = random.normal(mu_1, sigma_1, N)
gauss_2 = random.normal(mu_2, sigma_2, N)
gauss_2d = [gauss_1, gauss_2]

"""a)#####################################################################"""
print "a)"
print "La covarianza es:", cov(gauss_1, gauss_2)
print "El coeficiente de correlacion es:", pearsonr(gauss_1, gauss_2)[0]


"""b)#####################################################################"""
def ellipse_up(x, a, b):
    return sqrt(1-((x-3)/a)**2)*b**2+3
    
def ellipse_down(x, a, b):
    return -sqrt(1-((x-3)/a)**2)*b**2+3
    
def count(a, b, gau_1, gau_2):
    """Returns the amount of items in gau that return true from condition"""
    i = 0
    c = 0
    for x in gau_2:
        if (gau_1[c]-3)**2/a**2<=1:
            if abs(x-3)<=sqrt((1-((gau_1[c]-3)/a)**2)*b**2):
                i+=1
            else:
                i+=0
        else:
            i+=0
        c+=1
    return i

numb = count(sigma_1, sigma_2, gauss_1, gauss_2)
numb2 = count(2*sigma_1, 2*sigma_2, gauss_1, gauss_2)
numb3 = count(3*sigma_1, 3*sigma_2, gauss_1, gauss_2)
numb4 = count(4*sigma_1, 4*sigma_2, gauss_1, gauss_2)
print "b)"
print "Numero de puntos en sigma                ", numb
print "Porcentaje de numero total               ", numb/N
print "Valor esperado de distribucion gaussiana  0.46607"
print "Numero de puntos en 2*sigma                ", numb2
print "Porcentaje de numero total               ", numb2/N
print "Valor esperado de distribucion gaussiana  0.91107"
print "Numero de puntos en 3*sigma                ", numb3
print "Porcentaje de numero total               ", numb3/N
print "Valor esperado de distribucion gaussiana  0.99461"
print "Numero de puntos en 4*sigma                ", numb4
print "Porcentaje de numero total               ", numb4/N
print "Valor esperado de distribucion gaussiana  0.99987"

"""c)####################################################################"""
print "c)"

def f(x, y):
    return 3*x+5*y
    
def stan(sigma_1, sigma_2, gau_1, gau_2):
    """Calculate standard derivation of f(x, y)"""
    return (3*sigma_1)**2+(5*sigma_2)**2-2*3*5*pearsonr(gau_1, gau_2)[0]
    
print "La varianza de f(x,y) de los datos es:", var(f(gauss_1, gauss_2))
print "La varianza de f(x,y) de la propagacion de errores es:", stan(sigma_1, sigma_2, gauss_1, gauss_2)
    
"""d)####################################################################"""

print "d)"
print "Experimento igual con una rotacion de los datos de 30 grados"
### Rotation der Punktwolke
def cart2pol(x, y):
    rho = sqrt((x)**2 + (y)**2)
    phi = arctan2(y, x)
    return(rho, phi)
    
rho, phi = cart2pol(gauss_1-mu_1, gauss_2-mu_2)

def pol2cart(rho, phi):
    x = rho * cos(phi-theta)+mu_1
    y = rho * sin(phi-theta)+mu_2
    return(x, y)

gauss_1rot, gauss_2rot = pol2cart(rho, phi)
covarianz = pearsonr(gauss_1rot, gauss_2rot)[0]
print "La covarianza es:", cov(gauss_1rot, gauss_2rot)
print "El coeficiente de correlacion es:", covarianz

numb_rot = count(sqrt(var(gauss_1rot)), sqrt(var(gauss_2rot)), gauss_1rot, gauss_2rot)
numb_rot2 = count(2*sqrt(var(gauss_1rot)), 2*sqrt(var(gauss_2rot)), gauss_1rot, gauss_2rot)
numb_rot3 = count(3*sqrt(var(gauss_1rot)), 3*sqrt(var(gauss_2rot)), gauss_1rot, gauss_2rot)
numb_rot4 = count(4*sqrt(var(gauss_1rot)), 4*sqrt(var(gauss_2rot)), gauss_1rot, gauss_2rot)
#code fuer wolfram aplha: int (1/(2*pi*sqrt(1-0.851²))*exp(-0.5/(1-0.851²)*(x²+y²-2*0.851*x*y))) dx dy, x=-4 to 4, y=-4 to 4
print "Numero de puntos en sigma                ", numb_rot
print "Porcentaje de numero total               ", numb_rot/N
print "Valor esperado de distribucion gaussiana  0.57734"
print "Numero de puntos en 2*sigma                ", numb_rot2
print "Porcentaje de numero total               ", numb_rot2/N
print "Valor esperado de distribucion gaussiana  0.93188"
print "Numero de puntos en 2*sigma                ", numb_rot3
print "Porcentaje de numero total               ", numb_rot3/N
print "Valor esperado de distribucion gaussiana  0.99555"
print "Numero de puntos en 2*sigma                ", numb_rot4
print "Porcentaje de numero total               ", numb_rot4/N
print "Valor esperado de distribucion gaussiana  0.99989"

sigma_u = (sigma_1**2*(cos(theta))**2+sigma_2**2*(sin(theta))**2)#/((cos(theta))**2-(sin(theta))**2)
print sigma_u
sigma_v = (sigma_2**2*(cos(theta))**2+sigma_1**2*(sin(theta))**2)#/((cos(theta))**2-(sin(theta))**2)
print sigma_v

u=(sqrt(var(gauss_1rot))**2*(cos(theta))**2+sqrt(var(gauss_2rot))**2*(sin(theta))**2)
print u
v=(sqrt(var(gauss_2rot))**2*(cos(theta))**2+sqrt(var(gauss_1rot))**2*(sin(theta))**2)
print v
print "La varianza de los datos es:", var(f(gauss_1rot, gauss_2rot))
print "La varianza de f(x,y) de la propagacion de errores es:", stan(u, v, gauss_1rot, gauss_2rot)

print "El valor sigma_u es:", var(gauss_1rot)
print "El valor sigma_v es:", var(gauss_2rot)
print "El angulo es:", 180/pi*arcsin(2*covarianz*sqrt(var(gauss_1rot))*sqrt(var(gauss_2rot))/(sigma_1**2-sigma_2**2))/2

"""
plt.figure(1)                                    
plt.subplot(111)
plt.axis([-6, 12, -6, 12])   
plt.xlabel("x")
plt.ylabel("y")
plt.plot(gauss_1, gauss_2, linestyle='none', marker='.', ms=0.5)
arr = linspace(-sigma_1+3, sigma_1+3, 1000)
plt.plot(arr, ellipse_up(arr, sigma_1, sigma_2), ms=4, color="y")
plt.plot(arr, ellipse_down(arr, sigma_1, sigma_2), ms=4, color="y")
"""

plt.figure(1)                                  
plt.subplot(111)
plt.axis([-6, 12, -6, 12])       
plt.xlabel("x")
plt.ylabel("y")
plt.plot(gauss_1rot, gauss_2rot, linestyle='none', marker='.', ms=1)
arr = linspace(-sigma_1+3, sigma_1+3, 1000)
#plt.plot(arr, ellipse_up(arr, sigma_1, sigma_2), ms=4, color="y")
#plt.plot(arr, ellipse_down(arr, sigma_1, sigma_2), ms=4, color="y")


plt.draw()
plt.show()