#!/usr/bin/python3

# 1
age = 44
# 2
height = 1.8
# 3
comp = complex(age, height)
print(comp)

# 4
# base = input('Enter base: ')
# height = input('Enter height: ')
# print(f'The area of the triangle is {int(base) * int(height)}')
# 5
# a = input('Enter side a: ')
# b = input('Enter side b: ')
# c = input('Enter side c: ')
# print(f'The perimeter of the triangle is {int(a) + int(b) + int(c)}')
# 6
# length = input('Enter length: ')
# width = input('Enter width: ')
# print(f'The perimeter of the rectangle is {int(length) + int(width)}')
# 7
# radius = float(input('Enter radius: '))
# area = 3.14 * radius ** 2
# circumference = 2 * 3.14 * radius
# print(f'Area is {area}, Circumference is {circumference}')


# 8
# Calculate the slope, x-intercept and y-intercept of y = 2x - 2
# y = mx+b
y = '2x-2'
m1 = float(y[0])

x = [0, 1, 2, 3]


def gety(numsx) -> list:
    nums, i = [], 0
    while i < len(numsx):
        nums.append(2 * (numsx[i]) - 2)
        i += 1
    return nums


def makey(numx) -> int:
    return 2 * numx - 2


y = list(map(makey, x))
# y = gety(x)

slope = (y[2] - y[1]) / (x[2] - x[1])
x_int = 0, y[x.index(0)]
y_int = x[y.index(0)], 0

print(f'Slope is {m1}\nx-intercept is {x_int}\ny-intercept is {y_int}')

# 9
# Slope is (m = y2-y1/x2-x1). Find the slope and
# Euclidean distance between point (2,2) and point (6,10)
p1 = (2, 2)
p2 = (6, 10)
m = p2[1] - p1[1] / p2[0] - p1[0]
ed = ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
print(f'The slope is {m.__round__(2)} and the euclidian distance is {ed.__round__(2)}')

# 10
# Compare the slopes in tasks 8 and 9

# 11
# Calculate the value of y (y = x^2 + 6x + 9)
#

# 12
# Find the length of 'python' and 'dragon'
# and make a falsy comparison statement
print(len('python') != len('dragon'))  # False

# 13
# Use 'and' operator to check if 'on' is found
# in both 'python' and 'dragon'
is_present = 'on' in 'python' and 'on' in 'dragon'
print(is_present)  # True

# 14
# I hope this course is not full of jargon
# Use in operator to check if jargon is in the sentence
is_jargon = 'jargon' in 'I hope this course is not full of jargon'
print(is_jargon)  # True

# 15
# There is no 'on' in both dragon and python
print('on' not in 'dragon' and 'on' not in 'python')  # False

# 16
# Find the length of the text python and convert
# the value to float and convert it ot string
word_length = str(float(len('python')))
print(word_length)  # 6.0

# 17
# Even numbers are divisible by 2 and the remainder is zero.
# How do you check if a number is even or not in python?
num = input('Enter a number: ')
is_even = int(num) % 2 == 0

# 18
# Check if the floor division of 7 by 3 is equal
# to the int converted value of 2.7
is_equal = 7 // 3 == int(2.7)
print(is_equal)  # True

# 19
# Check if type of '10' is equal to type of 10
print(f'{type("10") == type(10)}')  # False


# 20
# Check if int('9.8') is equal to 10
# print(f'{int("9.8") == 10}')

# 21
# Write a script that prompts the user to enter
# hours and rate per hour. Calculate pay of the person.
hrs = int(input('Enter hours: '))
rph = float(input('Enter rate per hour: '))
pay = hrs * rph
print(f'Your weekly earning is {pay}')

# 22
# Write a script that prompts the user to enter number of years.
# Calculate the number of seconds a person can live.
yrs_lived = int(input('Enter the number of years you have lived: '))
print(f'You have lived for {yrs_lived*365*24*60*60} seconds')

# 23
print(
    '''
        1   1   1   1   1
        2   1   2   4   8
        3   1   3   9   27
        4   1   4   16  64
        5   1   5   25  125   
    '''
)
