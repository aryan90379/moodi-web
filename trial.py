from numpy import *
from pylab import *
from matplotlib import *
# x = linspace(1,10, 100)
# plot(x, log(x), "g", linewidth=3)
# plot(x, log10(x),'r', linewidth=2)
# legend(['log(x)', 'ln(x)'],loc="best")
# annotate('log(x)', xy=(3,1.5))
# annotate('ln(x)', xy=(4,.75))
# title('Logarithm functions plot')
# show()

# x = linspace(0, 1, 50)
# y = linspace(0, 2, 100)
# plot(x, y)
# show()

def except_last_two(L):
  return L[:-2]


X = [1,2,3,4,5,6,7,8,9]
print(except_last_two(X)) # [1, 2, 3, 4, 5, 6, 7]