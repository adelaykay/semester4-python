# def decorator_with_parameters(function):
#     def wrapper_accepting_paramaters(par1, par2, par3):
#         function(par1, par2, par3)
#         print("I live in {}".format(par3))
#     return wrapper_accepting_paramaters


# @decorator_with_parameters
# def print_full_names(first_name, last_name, country):
#     print("I am {}. I love to teach.".format(first_name, last_name, country))


# print_full_names("Adeleke", "Olasope", "Nigeria")

# Built-in functions
# def square(x):
#     return x ** 2


from functools import reduce

numbers = [1, 2, 3, 4, 5]
# num_square = map(square, numbers)
# num_square = map(lambda x: x ** 2, numbers)
# print(list(num_square))

numbers_str = ['1', '2', '3', '4', '5']
# numbers_int = map(int, numbers_str)
# print(list(numbers_int))

names = ['Adeleke', 'Olasope', 'Olaoluwa']


# def change_to_upper(name):
#     return name.upper()


# names_upper_cased = map(change_to_upper, names)
# names_upper_cased = map(lambda name: name.upper(), names)
# print(list(names_upper_cased))

# even_numbers = filter(lambda x: x % 2 == 0, numbers)
# print(list(even_numbers))


# def is_name_long(name):
#     if len(name) > 7:
#         return True


# long_name = filter(is_name_long, names)
# long_name = filter(lambda name: len(name) > 7, names)
# print(list(long_name))

def add_two_nums(x, y):
    return int(x) + int(y)


total = reduce(add_two_nums, numbers_str)
print(total)
