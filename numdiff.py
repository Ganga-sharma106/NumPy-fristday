import numpy as np

arr = np.array([10, 15, 25, 5])

newarr = np.diff(arr)

print(newarr)
print()


arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr, n=2)
print(newarr)
print()

newarr = np.diff(arr, n=3)
print(newarr)
