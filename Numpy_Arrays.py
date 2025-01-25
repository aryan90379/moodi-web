# from numpy import *
import numpy as np
from mathfunction import *
pi = np.pi
x = np.linspace(-5*pi, 5*pi, 50)
# print(x.size)   # print the size of the array
# print(x.shape)  # print the shape of the array
# print(x.ndim)   # print the dimension of the array
print("datatype of the arrya is : ",x.dtype)  # print the data type of the array
# print(x.itemsize) # print the size of each item in the array
#itemsize measures teh number of bytes  in each element of the array
#float64 is the default data type for numpy arrays
# print(x)

# shape can change as long as the number of elements in the array remains the same

a = np.array([1,2,3, 4])
b = np.array([2,3,4,5])
# print(a.dtype)
# print(b.dtype)
# # print(a[0])
# # print(a[-1])
# # a[0] = 100
# # print(a)
# # print(a+b)
# # print(a*b)
# print(a/b)





# ////////////     some other operations     ////////////
x = np.linspace(0.0,10.0,200)
x*= (2*pi)/10
y = np.sin(x)
y = np.cos(x)
x[0] = -1
# print(x[0],x[-1])
# print(x[199])

# /////////////////// Size rank and Shape of an array ///////////////////
x = np.array([1,2,3,4,5])  #int data type   
x = np.array([1.0,2,3,4,5])

# print(x.size)   # print the size of the array
# print(x.dtype)  # print the data type of the array
# print(x.shape)  # print the shape of the array (1D array) 
# print(x.ndim)   # print the dimension of the array
# print(x.itemsize) # print the size of each item in the array
# print(x.nbytes)   # print the total size of the array in bytes
# print(rank(x))    # print the rank of the array


#/////////////////////// Multi dimension Arrays  ////////////////////////
a =   np.array([[1,2,3],[4,5,6],[12,84,91]])  #(rows, columns)
# print(a.shape) # print the shape of the array (2D array) ex. (3,3)
# print(a[1,2])  # print the element at row 2 and column 3
# print(a[2,1])  # print the element at row 3 and column 2
# a[1,2] = -1
# print(a[1])   # print the second row
# a[0] = 0
# print(a[0])      # print the array
# print(a[0,1:12]) # print the elements in the first row from column 2 to 3
# print(a[1:,1:])  # print the elements in the secṇond and third row from column 2 to 3
# print(a[:,1])   # print the elements in the first column
print(a[0::2,0::2]) 
a[0::2,0::2] = 2837
print(a)
print(rank(a))    # print the rank of 