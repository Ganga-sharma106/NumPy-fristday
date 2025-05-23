import numpy as np

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)
print()


arr = np.array([41, 42, 43, 44])

# empty list
filter_arr = []

for element in arr:
  
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
print()

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# empty list
filter_arr = []

for element in arr:
  
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
print()


arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
print()

arr = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = arr % 2 == 0

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
print()

arr = np.array(['a', 'b', 'c'])
x = arr[[True, False, True]]
print(x)
print()