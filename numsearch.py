import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)
 # retunr [3,5,6] means that 4 is present in 3,5,6 index.
print(x)
print()

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0) #even

print(x)
print()

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 1) #odd
print(x)
print()

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)
print(x)
print()

x = np.searchsorted(arr, 3)
print(x)
print()

arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='left')
print(x)
print()

arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')
print(x)

arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)
print()

arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 8])
print(x)
print()