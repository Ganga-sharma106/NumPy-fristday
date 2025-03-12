import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)  #return (2,4) means - 2 rows and 4 columns in tuples form 
print()


arr = np.array([[1, 2, 3, 4 ,0], [5, 6, 7, 8,4]])

print(arr.shape)
print()

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)
print()

arr = np.array([1, 2, 3, 4], ndmin=4)
print(arr)
print('shape of array :', arr.shape)
print()

arr = np.array([1, 2, 3, 4], ndmin=1)
print(arr)
print('shape of array :', arr.shape)
print()

arr = np.array([1, 2, 3, 4], ndmin=2)
print(arr)
print('shape of array :', arr.shape)
print()