import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr)
print()

print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print()

print(arr[1] + arr[2])
print(arr[2] - arr[3])
print(arr[2] * arr[3])
print(arr[2] / arr[3])
print(arr[2] % arr[3])
print()

# Access 2-D Arrays
ar2 = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', ar2[0, 1])
print()

print('2nd element on 1st row: ', ar2[1, 2])
print()

# Access 3-D Arrays
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])
print()

print(arr[0, 0, 1])
print()

print(arr[1, 1, 1])
print()

# Negative Indexing

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 1st dim: ', arr[0, -2])
print()

print('Last element from 2nd dim: ', arr[1, -1])