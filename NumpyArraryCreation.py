import numpy as np
a = np.array([1, 2, 3], dtype=float)
b = np.array([[1, 2, 3], [4, 5, 6]], dtype=float)

c = np.array([2,0,1])
d = np.array([[1,2,3],[4,5,6],[7,8,9]])
e = np.array([[8,3,9],[9,4,8],[7,2,0]])
print(a.dtype)
np.ones_like(a)
print(np.ones_like(a))
print(np.ones((2,3)))
print("soo our identtity matrix is: ",np.identity(3))
# print(np.sum(b,axis=0)) # sum of columns
# print(np.sum(b,axis=1)) # sum of rows
print("product stuff now")
print(np.product(b,axis=0)) # sum of columns
print(np.product(b,axis=1)) # sum of rows
print(np.dot(a,c))
print(np.dot(d,e)) # matrix multiplication

# ///////////////////////////////// Loadtxt /////////////////////////////////
x = np.loadtxt('pendulum.txt', delimiter=',') # load data from file pendulum.txt    
print(x.shape)
print(x)

x,y = np.loadtxt('pendulum.txt', delimiter=',', unpack=True) # load data from file pendulum.txt
print(x.shape)
