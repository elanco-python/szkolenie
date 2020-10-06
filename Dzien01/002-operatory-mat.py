import math

"""
Operatory matematyczne
"""

x, y = 10, 3
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y)
print(x%y)

print(pow(x, y))
print(x**y)
print(math.pow(x,y))

result = int(math.pow(x,y))
result = str(result)
result = float(result)
print(type(result))

print("ABC" + "2")
print("ABC" * 3)
print("=" * 60)