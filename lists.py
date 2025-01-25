from numpy import *
import matplotlib.pyplot as plt
from pylab import *

mtlist = []
print(mtlist)
p = [2,6,2,8,4,5]
print(p[0]+p[1]+p[2])
print(p[2:5])
print('p[0:-1] = ',p[0:-1])
print('p[1:] = ',p[1:])
print(p[-1])
print(p[0:4:3]) # start, end, step
print(p[0::2]) # start, end, step
print(p[::2]) # start, end, step
print(p[::-1]) # reverse the list
# p.append(100)
b = [92,24,56]
c = p + b
print(c)
p.append(100)
print(p)
