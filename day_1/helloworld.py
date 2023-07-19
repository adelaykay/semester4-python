import math

# Arithmetic Operations

print(3+4) # Addition (7)

print(3-4) # Subtraction (-1)

print(3*4) # Multiplication (12)

print(3%4) # Modulus (3)

print(3/4) # Division (0.75)

print(3**4) # Exponentiation (81)

print(3//4) # Floor / Integer Division (0)

# Data Types
print('Adeleke') # str
print('Olasope') # str
print('Nigeria') # str
print('I am enjoying 30 days of python') # str
print(type(10)) # int
print(type(9.8)) # float
print(type(3.14)) # float
print(type(4-4j)) # complex
print(type(['Adeleke','Olaolu','Olasope'])) # list
print(type('Adeleke')) # str
print(type('Olasope')) # str
print(type('Canada')) # str

# Exercise Level 3
################################################################
# 1
# Integer
age = 30
print('age: ', age)
# Float
pi = 3.14
print('pi: ', pi)
# Complex
data = 2+3j
print('data: ', data)
# String
name = 'Zuckerberg'
print('name: ', name)
# Boolean
isDefined = True
print('isDefined: ', isDefined)
# List
cars = ['citroen', 'audi', 'mercedes', 'bmw', 'peugeot']
print('cars: ', cars)
# Tuple
trinity = ('father', 'son', 'holy spirit')
for person in trinity:
  print('God the ', person)
# Set
plang = {'java', 'python', 'javascript', 'java', 'c++', 'python'}
for lang in plang:
  print(lang)
# Dictionary
pairs = {
  1: "angel",
  "orange": [2,3,4],
  True: False,
  12: plang
}
print(pairs.get(1))
print(pairs.get('orange'))
print(pairs.get(True))
print(pairs.get(12))

################################################################
# 2
p = (2,3)
q = (10, 8)
# eucl = math.dist(p, q)
eucl = (((p[0] - q[0]) ** 2) + ((p[1] - q[1]) ** 2)) ** 0.5
print('Euclidian distance between points (2,3) and (10,8) is: ', eucl)