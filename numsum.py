import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.add(arr1, arr2)
print(newarr)
print()

newarr = np.sum([arr1, arr2])
print(newarr)
print()


newarr = np.sum([arr1, arr2], axis=1)
print(newarr)
print()

arr = np.array([1, 2, 3])
newarr = np.cumsum(arr)   # means [1,1+2,1+2+3]
print(newarr)
print()