from numpy import random

x = random.randint(100)
print(x)
print()

x=random.randint(100, size=(20))
print(x)
print()

x = random.randint(100, size=(3, 5))
print(x)
print()

x = random.randint(100, size=(5, 5))
print(x)
print()


x = random.rand()
print(x)
print()

x = random.rand(5)
print(x)
print()

x = random.rand(3, 5)
print(x)
print()

x = random.choice([3, 5, 7, 9])
print(x)
print()

x = random.choice([3, 5, 7, 9], size=(2, 5))
print(x)
print()
