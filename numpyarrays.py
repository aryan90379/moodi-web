from pylab import * # basically import everything
from mathfunction import *
from jupyter import *


import time
from datetime import datetime
t = [0.90,1.19,1.30,1.47,1.58,1.77,1.83]
t = array(t)
tsq = t**2
# print(tsq)
L = [0.2,0.3,0.4,0.5,0.6,0.7,0.8]
# plot(L,tsq,'b',label = 'T^2 vs L')
# show()

# t = range(0,10000)
# tsq = Arrsq(t)
# print(tsq,time.time()) # this is slower than the array function

# t = array(t)
# tsq = t**2
# print(tsq,time.time()) # this is faster than the Arrsq function

# %timeit Arrsq(t)
h = range(40,50)
print(array(h))



