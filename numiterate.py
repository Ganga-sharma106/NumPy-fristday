import numpy as np

# 1-D array
arr = np.array([1, 2, 3])
for x in arr:
  print(x)
print()

# 2-D Array
arr = np.array([[1, 2, 3], [4, 5, 6]])  # print in list form 
for x in arr:
  print(x)
print()

# Iterate each element 
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  for y in x:
    print(y)
print()

# 3-D Arrays -  In this condtiton ,it prints 2-d array
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
    print("x represents the 2-D array:")
    print(x)
print()

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
  for y in x:
    for z in y:
      print(z)
print()

# also iterate each value using "nditer()" 
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
  print(x)
print()

# Iterating Array With Different Data Types
arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)
print()

# Iterating With Different Step Size
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):
  print(x)
print()

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::3]):
  print(x)
print()

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::1]):
  print(x)
print()

#Enumerated Iteration Using ndenumerate() 
# Enumerate on following 1D arrays elements:  
arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
  print(idx, x)
print()

# Enumerate on following 2D arrays elements:
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
  print(idx, x)
print()