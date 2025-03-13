import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

newarr = np.add(arr1, arr2)

print(newarr)
print(type(newarr))
print()

newarr = np.subtract(arr1, arr2)
print(newarr)
print()

newarr = np.multiply(arr1, arr2)
print(newarr)
print()

newarr = np.divide(arr1, arr2)
print(newarr)
print()

newarr = np.power(arr1, arr2)
print(newarr)
print()

newarr = np.mod(arr1, arr2)  #Return remainder 
print(newarr)
print()

newarr = np.remainder(arr1, arr2)  #- Return remainder 
print(newarr)
print()

newarr = np.divmod(arr1, arr2)
print(newarr)
print()

arr = np.array([-1, -2, 1, 2, 3, -4])
newarr = np.absolute(arr)
print(newarr)

