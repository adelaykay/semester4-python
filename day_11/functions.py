''' Functions '''


# def add_num():
#     ''' Adds two numbers together '''
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter another number: "))
#     print(f'{num1} + {num2} = {num1 + num2}')


# def greetings(name):
#     ''' Returns a greeting message '''
#     message = f'{name}, Welcome to the python class'
#     return message


# def add_bonus(salary):
#     ''' Calcualtes 20% bonus and adds it to given salary '''
#     bonus = 0.2 * salary
#     return salary + bonus


# def sum_of_numbers(n):
#     total = 0
#     for num in range(n + 1):
#         total += num
#     return total


# print(sum_of_numbers(10000))


# def calculate_age():
#     ''' A function that prints age. takes year as input and return age. '''
#     current_year = 2023
#     current_month = 'september'
#     months = {
#       'january': 1,
#       'february': 2,
#       'march': 3,
#       'april': 4,
#       'may': 5,
#       'june': 6,
#       'july': 7,
#       'august': 8,
#       'september': 9,
#       'october': 10,
#       'november': 11,
#       'december': 12
#     }
#     year_of_birth = int(input('What year were you born?: '))
#     month_of_birth = input('What month were you born?: (eg. January)').lower()
#     age_in_years = current_year - year_of_birth
#     if months[month_of_birth] > months[current_month]:
#         age_in_years -= 1
#         months_suffix = 11 - months[month_of_birth] - months[current_month]
#         if age_in_years > 0:
#             print(f'You are {age_in_years} years and {abs(months_suffix)} months old')
#         else:
#             print('The beautiful ones are not yet born!')
#     elif months[month_of_birth] <= months[current_month]:
#         months_suffix = months[current_month] - months[month_of_birth]
#         if age_in_years > 0:
#             print(f'You are {age_in_years} years and {abs(months_suffix)} months old')
#         else:
#             print(f'You are {abs(months_suffix)} months old')


# calculate_age()


# Exercises Day 11
# Level 1
# 1
def add_two_numbers(a, b):
    ''' returns the addition of two numbers '''
    return a + b


print(f'1. {add_two_numbers(3, 5)}')


# 2
def area_of_circle(radius):
    ''' returns the area of a circle '''
    PI = 3.14
    return PI * radius * radius


print(f'2. {area_of_circle(5)}')


# 3
def add_all_nums(*args):
    ''' adds all numbers passed as argument '''
    total = 0
    for item in args:
        if isinstance(item, (int, float)):
            total += item
        else:
            return Exception(f'Invalid argument "{item}", only numbers are allowed')
    return total


print(f'3. {add_all_nums(3, 5, 7, "a")}')


# 4
def cel_to_far(temp_in_cel):
    ''' converts celsius to farenheit '''
    return temp_in_cel * (9 / 5) + 32


print(f'4. 30C = {cel_to_far(30)}F')


# 5
def check_season(month):
    ''' returns the season the month belongs to '''
    autumn = ['september', 'october', 'november']
    winter = ['december', 'january', 'february']
    spring = ['march', 'april', 'may']
    summer = ['june', 'july', 'august']

    if month in autumn:
        return 'autumn'
    if month in winter:
        return 'winter'
    if month in spring:
        return 'spring'
    if month in summer:
        return 'summer'
    return f'{month.title()} is not a valid month'


print(f'5. {check_season("january")}')


# Level 2
# 1
def evens_and_odds(num):
    ''' returns number of even and odd numbers in num '''
    count_evens, count_odds = 0, 0
    for i in range(num + 1):
        if i % 2 == 0:
            count_evens += 1
        else:
            count_odds += 1
    return f'The number of odds is {count_odds}\n   The number \
of evens is {count_evens}'


print(f'1. {evens_and_odds(100)}')


# 2
def is_empty(anything):
    ''' checks if anything is something or nothing '''
    if anything:
        return 'something'
    return 'nothing'


print(f'2. Nothing is {is_empty("nothing")}')


# 3
def calculate_mean(*nums):
    ''' returns the mean of numbers in argument nums '''
    return sum(nums) / len(nums)


def calculate_median(*nums):
    ''' returns the median of numbers in argument nums '''
    s_nums = sorted(nums)
    if len(s_nums) % 2 == 1:
        return s_nums[len(nums) // 2]
    else:
        return (s_nums[(len(nums) - 1) // 2] + s_nums[len(nums) / 2]) / 2


def calculate_mode(*nums):
    ''' returns the mode of numbers in argument nums '''
    count, mode_count, mode_num = 1, 1, nums[0]
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            count += 1
        elif count > mode_count:
            mode_count = count
            mode_num = nums[i - 1]
            count = 1
        elif count <= mode_count:
            count = 1
    return mode_num


def calculate_range(*nums):
    ''' returns the range of numbers in argument nums '''
    s_nums = sorted(nums)
    range_of_nums = s_nums[0] - s_nums[-1]
    return range_of_nums


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(f'3. Mean = {calculate_mean(numbers)}')