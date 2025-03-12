import numpy

import numpy as np

ar = np.array([6,7,8,9])
print(ar)
print()

arr = numpy.array([1,2,3,4])
print(arr)
print(type(arr))
print()

arr1 = np.array((1, 2, 3, 4, 5))
print(arr1)
print(type(arr1))
print()

# 0-D Arrays
arr2 = np.array(42)
print(arr2)
print()

# 1-D Arrays
arr3 = numpy.array([1,2,3,4])
print(arr3)
print()

# 2-D Arrays
ar5 = np.array([[8,9,0] , [3,2,1]])
print(ar5)
print()


# 3-D arrays
ar6 = np.array([[[5,6,7] , [9,8,3] , [1,2,4]]])
print(ar6)
print()

# Check Number of Dimensions
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
print()


# Higher Dimensional Arrays
arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)
print()

print(np.__version__)