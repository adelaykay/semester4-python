import random
import string


# Exercises: Day 12
# Exercises: Level 1
# 1.	Write a function which generates a six digit/character random_user_id.
def random_user_id(length):
    """Generates a random user_id"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


# print(random_user_id(6))


# print(random_user_id());
#   '1ee33d'
# 3.	Modify the previous task. Declare a function named user_id_gen_by_user.
#       It doesn’t take any parameters but it takes two inputs using input().
#       One of the inputs is the number of characters and the second input is
#       the number of IDs which are supposed to be generated.
# print(user_id_gen_by_user()) # user input: 5 5
# #output:
# #kcsy2
# #SMFYb
# #bWmeq
# #ZXOYh
# #2Rgxf

def user_id_gen_by_user():
    """Generates the given number of IDs"""
    num_of_chars = int(input('How long do you want the generated id to be?'))
    num_of_ids = int(input('How many IDs?'))
    id_list = []

    for i in range(num_of_ids):
        print(random_user_id(num_of_chars))
    return ''


# print(user_id_gen_by_user()) # 16 5


# #1GCSgPLMaBAVQZ26
# #YD7eFwNQKNs7qXaT
# #ycArC5yrRupyG00S
# #UbGxOFI7UXSWAyKN
# #dIV0SSUTgAdKwStr
# 3.	Write a function named rgb_color_gen.
#       It will generate rgb colors (3 values ranging from 0 to 255 each).
# # rgb(125,244,255) - the output should be in this form
def color_gen():
    """ Generates a random color """
    return random.randint(0, 255)


def rgb_color_gen():
    """Generates an RGB color"""
    rgb_color = []
    for i in range(3):
        rgb_color.append(color_gen())
    return 'rgb' + str(tuple(rgb_color))


# Exercises: Level 2
# 1.	Write a function list_of_hexa_colors which returns any number of hexadecimal colors
#       in an array (six hexadecimal numbers written after #.
#       Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f.
#       Check the task 6 for output examples).
def hexa_color_gen():
    """Generates a hexadecimal color"""
    color = '#'
    for i in range(6):
        color += hex(color_gen())[-2:-1]
    return color


def list_of_hexa_colors(num):
    """Generates a list of hexadecimal colors"""
    hexa_colors = []
    for i in range(num):
        hexa_colors.append(hexa_color_gen())
    return hexa_colors


# print(list_of_hexa_colors(4))


# 2.	Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(num):
    """Generates a list of RGB colors"""
    rgb_list = []
    for i in range(num):
        rgb_list.append(rgb_color_gen())
    return rgb_list


# print(list_of_rgb_colors(3))


# 3.	Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(color_format, num):
    """Generates the given number of hexa or rgb colors"""
    if color_format == 'rgb':
        print(list_of_rgb_colors(num))
    elif color_format == 'hexa':
        print(list_of_hexa_colors(num))


# generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b']
# generate_colors('hexa', 1) # ['#b334ef']
# generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80']
# generate_colors('rgb', 1)  # ['rgb(33,79, 176)']


# Exercises: Level 3
# 1.	Call your function shuffle_list, it takes a list as a parameter,
#       and it returns a shuffled list
def shuffle_list(*lst):
    """Shuffle a list"""
    return random.sample(lst, len(lst))


# print(shuffle_list(2,3,4,True,True,False, 0.4, ('Adeleke')))


# 2.	Write a function which returns an array of seven random numbers in a range of 0-9.
#       All the numbers must be unique.
def unique_random_numbers():
    """Generates an array of seven random single digit numbers"""
    numbers = list(range(10))
    unique_numbers = random.sample(numbers, 7)
    return unique_numbers


# print(unique_random_numbers())
