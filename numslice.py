import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])
print() 

# Slice = [start:End:Step]

print(arr[4:])
print()

print(arr[:4])
print()

print(arr[0:6:2])
print()

print(arr[::2])
print()

#[ start : stop ]
print(arr[-3:-1])
print(arr[-6:-1])
print(arr[-7:-1])
print(arr[-4:-2])
print()

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])
print(arr[0, 0:3])
print()

print(arr[0:2, 2])
print(arr[0:2, 1])
print(arr[0:2,4])
print()

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 1:4])
print(arr[0:2, 1:3])