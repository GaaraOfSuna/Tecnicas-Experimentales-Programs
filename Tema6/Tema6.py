# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 10:05:55 2015

@author: GAARA
"""

import numpy as np
from numpy.random import uniform, random_sample

from matplotlib import pyplot as plt

def decay(t, N_0, tau):
    return N_0*np.exp(-t/tau)
    
def prob(t, tau):
    return 1/tau*np.exp(-t/tau)

#Main
tau = 29/np.log(2)                      # mean lifetime
N_0=100000
# a)
tau_b=np.exp(np.log(tau)-np.log(0.83))
tau_c=np.exp(np.log(tau)-np.log(0.17))

print tau_b
print tau_c

"""
1/tau*np.exp(-t/tau)=(1/tau_b+1/tau_capt)*np.exp(-t*(1/tau_b+1/tau_capt))
1/tau*np.exp(-t/tau)=np.exp(-t/tau_b)*np.exp(-t/tau_capt)/tau_b+np.exp(-t/tau_b)*np.exp(-t/tau_capt)/tau_capt

np.exp(-t/tau_b)*np.exp(-t/tau_capt)/tau_b=0.83*1/tau*np.exp(-t/tau)
np.exp(-t/tau_b)*np.exp(-t/tau_capt)/tau_capt=0.17*1/tau*np.exp(-t/tau)

-t/tau_b-t/tau_capt-ln tau_b=ln 0.83-ln tau-t/tau

ln tau-ln 0.83=ln tau_b
"""

# b)

def mctimes(tau_b, tau_c):
    """Calculates the random time exponentiell distibution"""
    n=10000
    t_a=-np.log(np.random.uniform(0, 1, n))*tau_b
    t_b=-np.log(np.random.uniform(0, 1, n))*tau_c

    m = []
    count=0
    for i in np.arange(n):
        if t_a[i]<=t_b[i]:
            count=count+1
            m.append(t_a[i])
        else:
            m.append(t_b[i])
        
    M=np.sort(m)[::-1]
    return M, np.float32(count)/n
        
print mctimes(tau_b, tau_c)[1]
print 1-mctimes(tau_b, tau_c)[1]

plt.figure(1)
plt.subplot(111)
plt.axis([0, 200, 0, 0.025])
plt.xlabel('t en horas')
plt.ylabel('p(t) normed')
plt.hist(mctimes(tau_b, tau_c)[0], bins=50, normed=True, label='espectro de la variable t')
plt.plot(np.arange(200), prob(np.arange(200), tau), '-', label='1/tau*exp(-t/tau)')
plt.legend(loc=1)


plt.draw()
plt.show()

