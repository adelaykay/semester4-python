# Python Programming
################################
# Exercise Level 1

first_name = 'Adeleke'
last_name = 'Olasope'
full_name = first_name, ' ', last_name
country = 'United States'
city = 'Raleigh'
age = 18
year = 2023
is_married = False
is_true = True
is_light_on = False
is_employed, dob, fuel_price = False, '09-11-2015', 617.00

# Exercise Level 2
# 1 Data type of all variables declared in Level 1
print(
    'First Name: ', type(first_name),
    '\nLast Name: ', type(last_name),
    '\nFull Name: ', type(full_name),
    '\nCountry: ', type(country),
    '\nCity: ', type(city),
    '\nAge: ', type(age),
    '\nYear: ', type(year),
    '\nIs Married: ', type(is_married),
    '\nFuelPrice: ', type(fuel_price),
    '\nIs True: ', type(is_true),
    '\nIs Light On: ', type(is_light_on),
    '\nIs Employed: ', type(is_employed),
    '\nDate of Birth: ', type(dob),
)

# 2 Length of first name
print('Length of first name: ', len(first_name))

# 3 Compare length of first name with length of last name
print('First name: ', len(first_name), '\nLast name: ', len(last_name))

# 4
num_one, num_two = 5, 4
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

# 5
# radius = 30
pi = 3.14
radius = float(input('Enter radius: '))
area_of_circle = pi * (radius ** 2)
circum_of_circle = 2 * pi * radius
# ----------------------------------------------------------------
print('Area of circle: ' , area_of_circle)

# ----------------------------------------------------------------

# 6
first_name = input('Enter first name: ')
last_name = input('Enter last name: ')
country = input('Enter country: ')
age = int(input('Enter age: '))

print(help('keywords'))