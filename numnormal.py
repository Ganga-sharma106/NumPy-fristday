from numpy import random

x = random.normal(size=(2, 3))

print(x)
print()

x = random.normal(loc=1, scale=2, size=(2, 3))

print(x)
print()

# Visualization 
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(size=1000), hist=False)

plt.show()