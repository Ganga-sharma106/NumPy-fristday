from math import log
import numpy as np

nplog = np.frompyfunc(log, 2, 1)
print(nplog(100, 15))
print()

arr = np.arange(1,6)
print(np.log2(arr))
print()

print(np.log10(arr))
print()

print(np.log(arr))
print()