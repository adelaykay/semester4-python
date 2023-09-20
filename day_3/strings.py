#!/usr/bin/python3

# 1
my_age = 44

# 2
my_height = 1.8

# 3
comp = complex(my_age, my_height)
print(f'3. {comp}\n')
print('_______________________________________________')

# 4
base = input('Enter base: ')
height = input('Enter height: ')
print(f'4. The area of the triangle is {int(base)/2 * int(height)}\n')
print('_______________________________________________')

# 5
a = input('Enter side a: ')
b = input('Enter side b: ')
c = input('Enter side c: ')
print(f'5. The perimeter of the triangle is {int(a) + int(b) + int(c)}\n')
print('_______________________________________________')

# 6
length = input('Enter length: ')
width = input('Enter width: ')
print(f'6. The perimeter of the rectangle is {(int(length) + int(width)) * 2}\n')
print('_______________________________________________')

# 7
# Get the radius of a circle using prompt
# Calculate the area and circumference where pi=3.14
radius = float(input('Enter radius: '))
area = 3.14 * radius ** 2
circumference = 2 * 3.14 * radius
print(f'7. Area is {area}, Circumference is {circumference}\n')
print('_______________________________________________')


# 8
# Calculate the slope, x-intercept and y-intercept of y = 2x - 2
# y = mx+b
y = '2x-2'
m1 = float(y[0])

x = [0, 1, 2, 3]


def get_y(nums) -> list:
    # This function takes a list of numbers (nums)
    # iterates over each number in the list
    # finds 2 times the number minus 2
    # and appends the result to a new list new_nums
    new_nums, i = [], 0
    while i < len(nums):
        new_nums.append(2 * (nums[i]) - 2)
        i += 1
    return new_nums


def make_y(num) -> int:
    # This function takes a number num
    # and returns 2 times the number minus 2
    return 2 * num - 2


y = list(map(make_y, x))
# y = gety(x)

slope = (y[2] - y[1]) / (x[2] - x[1])
x_int = 0, y[x.index(0)]
y_int = x[y.index(0)], 0

print(f'8. Slope is {m1}\nx-intercept is {x_int}\ny-intercept is {y_int}\n')
print('_______________________________________________')

# 9
# Slope is (m = y2-y1/x2-x1). Find the slope and
# Euclidean distance between point (2,2) and point (6,10)
p1 = (2, 2)
p2 = (6, 10)
m2 = p2[1] - p1[1] / p2[0] - p1[0]
ed = ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
print(f'9. The slope is {m2:.2f} and the euclidian distance is {ed:.2f}\n')
print('_______________________________________________')
round()
# 10
# Compare the slopes in tasks 8 and 9
print(f'10. {m1 > m2}\n')
print('_______________________________________________')

# 11
# Calculate the value of y (y = x^2 + 6x + 9)
#
x = list(range(-10, 11))


def check_x(num) -> bool:
    """
    This function checks if the result of the
    quadratic equation num^2 + 6(num) + 9 is zero
    :param num: integer
    :return: boolean
    """
    return num ** 2 + 6 * num + 9 == 0


ans = list(filter(check_x, x))
print(f'11. {ans}\n')
print('_______________________________________________')

# 12
# Find the length of 'python' and 'dragon'
# and make a falsy comparison statement
print(f"12. {len('python') != len('dragon')}\n")  # False
print('_______________________________________________')

# 13
# Use 'and' operator to check if 'on' is found
# in both 'python' and 'dragon'
is_present = 'on' in 'python' and 'on' in 'dragon'
print(f'13. {is_present}\n')  # True
print('_______________________________________________')

# 14
# I hope this course is not full of jargon
# Use in operator to check if jargon is in the sentence
is_jargon = 'jargon' in 'I hope this course is not full of jargon'
print(f'14. {is_jargon}\n')  # True
print('_______________________________________________')

# 15
# There is no 'on' in both dragon and python
print(f"15.  {'on' not in 'dragon' and 'on' not in 'python'}\n")  # False
print('_______________________________________________')

# 16
# Find the length of the text python and convert
# the value to float and convert it to string
word_length = str(float(len('python')))
print(f'16. {word_length}\n')  # 6.0
print('_______________________________________________')

# 17
# Even numbers are divisible by 2 and the remainder is zero.
# How do you check if a number is even or not in python?
print('''
        This script checks if a number is even.
        True: the number is even
        False: the number is odd''')
num = input('Enter a number: ')
is_even = int(num) % 2 == 0
print(f'17. {is_even}\n')
print('_______________________________________________')

# 18
# Check if the floor division of 7 by 3 is equal
# to the int converted value of 2.7
is_equal = 7 // 3 == int(2.7)
print(f'18. {is_equal}\n')  # True
print('_______________________________________________')

# 19
# Check if type of '10' is equal to type of 10
print(f'19. {type("10") == type(10)}\n')  # False
print('_______________________________________________')

# 20
# Check if int('9.8') is equal to 10
# print(f'{int("9.8") == 10}')
aa = int(9.8)
ab = 10
print(f'20. {aa == ab}\n')
print('_______________________________________________')

# 21
# Write a script that prompts the user to enter
# hours and rate per hour. Calculate pay of the person.
hrs = int(input('Enter hours: '))
rph = float(input('Enter rate per hour: '))
pay = hrs * rph
print(f'21. Your weekly earning is {pay}\n')
print('_______________________________________________')

# 22
# Write a script that prompts the user to enter number of years.
# Calculate the number of seconds a person can live.
yrs_lived = int(input('Enter the number of years you have lived: '))
print(f'22. You have lived for {yrs_lived * 365 * 24 * 60 * 60} seconds\n')
print('_______________________________________________')

# 23
print('''
23.
        1   1   1   1   1
        2   1   2   4   8
        3   1   3   9   27
        4   1   4   16  64
        5   1   5   25  125   
    '''
)
print('_______________________________________________')
