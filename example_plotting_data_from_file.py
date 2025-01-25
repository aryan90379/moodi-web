from numpy import *
from pylab import *
x,y = loadtxt('pendulum.txt',delimiter=' ',unpack=True) # determine is to specify if the values are comma seperated or space separated
# print(x)
# plot(x,y,'.',color='red')
# show(ṇṇṇ

print(mean(x))
print(std(x))
a = array([[1,2,3],[4,5,6],[7,8,9]])
print(a[:2,:]) # first two rows and all columns , does not include the 3rd row
print(a.shape)