import numpy as np
def sqr(num):
    return num**2

def Arrsq(arr):
    return [sqr(num) for num in arr]

def sum(num1,num2):
    return num1+num2

def rank(array):
    """
    Returns the rank of the input:
    - If the input is 1D or higher, returns the number of dimensions (ndim).
    - If the input is 2D or higher, checks for matrix rank using linear algebra.
    """
    if array.ndim == 2:
        return np.linalg.matrix_rank(array)  # Matrix rank for 2D arrays
    else:
        return array.ndim  # Number of dimensions for 1D arrays

