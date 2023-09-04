''''
Decision Making
'''

# Question 1
age = int(input("Enter your age: "))

if age >= 18:
    print('You are old enough to drive')
else:
    print(f'You need {18-age} more year to drive')

# Question 2
my_age = 14

your_age = int(input("Enter your age: "))
year, diff = '', abs(your_age - my_age)
if your_age > my_age:
    if abs(your_age - my_age) > 1:
        year = 'years'
    else:
        year = 'year'
    print(f'Your are {diff} {year} older than me')
elif your_age == my_age:
    print('We are age mates')
else:
    if abs(your_age - my_age) > 1:
        year = 'years'
    else:
        year = 'year'
    print(f'I am {diff} {yr} older than you')

# Question 3
num_a = int(input('Enter number one: '))
num_b = int(input('Enter number two: '))

if num_a > num_b:
    print(f'{num_a} is greater than {num_b}')
elif num_a < num_b:
    print(f'{num_b} is greater than {num_a}')
else:
    print(f'{num_a} is equal to {num_b}')


# Exercises -  Level 2
# Question 1
grade = int(input('Enter grade: '))

if grade < 50:
    print(f'F')
elif 59 >= grade >= 50:
    print(f'D')
elif 69 >= grade >= 60:
    print(f'C')
elif 79 >= grade >= 70:
    print(f'B')
elif 100 >= grade >= 80:
    print(f'A')

# Question 2
autumn = ['september', 'october', 'november']
winter = ['december', 'january', 'february']
spring = ['march', 'april', 'may']
summer = ['june', 'july', 'august']

month = (input('Enter the month: ')).lower()

if month in autumn:
    print(f'{month.title()} is in Autumn')
elif month in winter:
    print(f'{month.title()} is in Winter')
elif month in spring:
    print(f'{month.title()} is in Spring')
elif month in summer:
    print(f'{month.title()} is in Summer')
else:
    print(f'{month.title()} is not a valid month')

# Question 3
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Enter a fruit name: ')
if fruit in fruits:
    print(f'That fruit already exists in the list')
else:
    fruits.append(fruit)
    print(f'{fruits}')

# Exercises - Level 3
person = {
  'first_name': 'Bola',
  'last_name': 'Tinubu',
  'age': 39,
  'country': 'Nigeria',
  'is_married': True,
  'skills': ['motivational speaking', 'auditing', 'farming'],
  'address': {
    'street': 'bourdillon',
    'zipcode': '101231'
  }
}

if 'skills' in person:
    print(f'{person['skills'])
