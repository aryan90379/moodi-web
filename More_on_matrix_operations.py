from numpy import array
from numpy.linalg import inv, det
from pylab import *

# Define a 5x5 invertible matrix
a = array([
    [2, 0, 1, 3, 5],
    [4, 1, 6, 0, 7],
    [3, 7, 2, 8, 1],
    [5, 4, 9, 6, 0],
    [1, 8, 0, 2, 3]
])
print("sum is ",sum(a))
# print("eigen value is ",eig(a)) gives a tuple     # wil give eigen vector and their corresponding vectors
# print(eigvals(a)) # will give only eigen values
# Check determinant

# /////////////// DIVIDING INTO EIGEN VALUES AND VECTORS ///////////////////////

ev, evec = eig(a)
# print("Eigen values:", ev)
# print("Eigen vectors:", evec)

# or print 

print(eig(a)[0]) # eigen values
print(eig(a)[1]) # eigen vectors
print("norm of the first eigen vector",norm(evec[0])) # norm of the first eigen vector
print("norm of the first eigen vector",norm([3,4])) # norm of the first eigen vector

print("single value decomposition",svd(a))


# print("Determinant:", det(a))



# Calculate inverse if determinant is non-zero
# if det(a) != 0:
#     print("Inverse:")
#     # print(inv(a))
# else:
#     print("Matrix is singular and cannot be inverted.")


#  for matricx mutliplacation use
# dot(a,b)

# print("dot product of a and its inverse",dot(a,inv(a))) # should be identity matrix

