# [i for i in iterable if condition]
#
# language = 'Python'
# lst = list(language)
# print(lst)
#
# lst2 = [i for i in language]
# print(lst2)

# squares = [i*i for i in range(11)]
# print(squares)

# numbers = tuple([(x, x**x) for x in range(11)])
# print(numbers)

# even_numbers = [i for i in range(21) if i % 2 == 0]
# print(even_numbers)

# positive_even_numbers = [i for i in range(21) if i % 2 == 0 and i > 0]
# print(positive_even_numbers)

# Lamdas
# def add_two_nums(a, b):
#     """adds two numbers"""
#     return a + b

# add_two_nums = lambda a, b: a + b  # add two numbers
# print(add_two_nums(23,54))

# self invoking lambda expression
# result = (lambda a, b: a + b)(40, 65)
# print(result)
# print((lambda a, b: a + b)(40, 65))

# square = (lambda x: x ** 2)(4)
# print(square)
#
# square_of_list = (lambda numbers: [x * x for x in numbers])(list(range(10)))
# print(square_of_list)

# def power(x):
#     return lambda n: x ** n
# print(power(4)(3))

# Exercises: Day 13
# 1.	Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
neg_and_zero = [number for number in numbers if number <= 0]
print(f'1. {neg_and_zero}')


# 2.	Flatten the following list of lists of lists to a one dimensional list :
#   	output
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
one_dime = [number for list_of_nums in list_of_lists for numbers in list_of_nums for number in numbers]
print(f'2. {one_dime}')


# 3.	Using list comprehension create the following list of tuples:
#   	[(0, 1, 0, 0, 0, 0, 0),
#   	(1, 1, 1, 1, 1, 1, 1),
#   	(2, 1, 2, 4, 8, 16, 32),
#   	(3, 1, 3, 9, 27, 81, 243),
#   	(4, 1, 4, 16, 64, 256, 1024),
#   	(5, 1, 5, 25, 125, 625, 3125),
#   	(6, 1, 6, 36, 216, 1296, 7776),
#   	(7, 1, 7, 49, 343, 2401, 16807),
#   	(8, 1, 8, 64, 512, 4096, 32768),
#    	(9, 1, 9, 81, 729, 6561, 59049),
#     (10, 1, 10, 100, 1000, 10000, 100000)]
# lst_of_tupes = []
# for i in range(11):
#     lst1 = []
#     lst1.append(i)
#     for j in range(6):
#         lst1.append(i ** j)
#     lst_of_tupes.append(tuple(lst1))

lst_of_tupes = [tuple([num]+[num**exp for exp in range(6)]) for num in range(11)]
print(f'3. {lst_of_tupes}')
# 4.	Flatten the following list to a new list:
#   	output:
#     [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
new_list = [[tup[0].upper(), tup[0][:3].upper(), tup[1].upper()] for lst in countries for tup in lst]
print(f'4. {new_list}')


# 5.	Change the following list to a list of dictionaries:
#   	output:
#   	[{'country': 'FINLAND', 'city': 'HELSINKI'},
#   	{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
#     {'country': 'NORWAY', 'city': 'OSLO'}]

lst_of_dicts = [{'country': tup[0].upper(), 'city': tup[1].upper()} for lst in countries for tup in lst]
print(f'5. {lst_of_dicts}')

# 6.	Change the following list of lists to a list of concatenated strings:
#     output
#     ['Omoefe Ugboma', 'David Smith', 'Donald Trump', 'Bill Gates']

names = [[('Omoefe', 'Ugboma')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
lst_of_strings = [' '.join(tups) for lst_of_tups in names for tups in lst_of_tups]
print(f'6. {lst_of_strings}')


# 28.	Write a lambda function which can solve a slope or y-intercept of linear functions.
