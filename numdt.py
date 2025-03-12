import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr)
print(arr.dtype)
print()

arr1 = np.array(['apple', 'banana', 'cherry'])
print(arr1.dtype)     
#o/p - <U6   #< → Little-endian byte order (used for memory storage, not relevant for most cases).
            # U → Unicode string (used to store text in NumPy arrays).
            #6 → Maximum string length (the longest word in the array has 6 characters)
print()

arr2 = np.array(['apple', 'banana', 'watermelon'])
print(arr2.dtype)  # op- <U10
print()  

import numpy as np

arr3 = np.array([1, 2, 3, 4], dtype='S')  # Print values in binary form 

print(arr3)
print(arr3.dtype)
print()

arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)
print()

arr6 = np.array([1.1, 2.1, 3.1])

newarr = arr6.astype('i')
# give int32 
print(newarr)
print(newarr.dtype)
print()

arr7 = np.array([1.1, 2.1, 3.1])

newarr = arr7.astype(int)
#give int64 
print(newarr)
print(newarr.dtype)
print()

arr = np.array([1, 0, 2])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)
print()

arr = np.array([-1, 0, 1])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)
print()

arr = np.array([1, 2, 3, 4], dtype='U')

print(arr)
print(arr.dtype)
print()

arr = np.array([1, 2, 3, 4], dtype='f')

print(arr)
print(arr.dtype)
print()