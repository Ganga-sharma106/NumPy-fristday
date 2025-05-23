import numpy as np

num1 = 4
num2 = 6
x = np.lcm(num1, num2)
print(x)
print()

arr = np.array([3, 6, 9])
x = np.lcm.reduce(arr)
print(x)
print()

arr = np.arange(1, 4)
x = np.lcm.reduce(arr)
print(x)
print()