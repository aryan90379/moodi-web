from matplotlib import *
from pylab import *
from numpy import *
L,t = loadtxt('pendulum.txt',unpack=True)
tsq = t*t
A = array([L,ones_like(L)]).T
# print(A)
result = lstsq(A, tsq, rcond=None)      
coef = result[0]    # the matrix contains [slope, intercept]
print(coef)
Tline = coef[0]*L + coef[1]
# print(Tline.shape)
# print(Tline)
plot(L, Tline, 'r', label='least square fit')
plot(L, tsq,color = "blue", label='Data')
show()