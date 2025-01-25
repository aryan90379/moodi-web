import numpy as np
from matplotlib import *
from pylab import * 
# np.random

# a = np.random.random(size=(100))
# b = np.random.random(size=(100))
# scatter(a,b)
# # plot(a,b)
# show()

# x,y = np.random.normal(size=(2,100))
# scatter(x,y)
# show()
# for i in range(5):
# img = np.random.random(size=(200,200,4))
# imshow(img)
# colorbar()
# show()        


b = identity(5000) 
print(b.size)  # tells you the size of the array
print(b.shape) # tells you the shape of the array
print(size(b)) # tells you the size of the array
# imshow(b)
# colorbar()
# show()

x = array([[1,2,3,4]])
# x[0][2] = 0
# print(x)    
x[0] = 0    # this will change the whole row to 0
print(x)


a = array([[0, 0, 0],
       [3, 4, 5],
       [0, 0, 0]])
print(a[1]*a[1]) # this will multiply the second row by itself

x = array(([1,2,3,4],[2,3,4,5]))
x[-2][-3] = 4 
print("the new array x is:",x)    # this will change the value of the first row, third column to 4