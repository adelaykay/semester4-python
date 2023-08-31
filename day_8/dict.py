'''


Dictionary Exercises
'''



# 1


dog = {}


print(f'1. Empty dictionary: {dog}')



dog['name'] = 'Oscar'


dog['color'] = 'black'


dog['legs'] = 3


dog['age'] = 14


print(f'2. Dog: {dog}')



# 3
student = {


  'first_name': 'Bola',


  'last_name': 'Tinubu',


  'gender': 'male',


  'age': 44,


  'marital_status': 'married',


  'country': 'Nigeria',


  'city': 'Lagos',


  'skills': ['Auditing'],


  'address': {


    'street': '45, Awolowo Avenue',


    'zipcode': 101282


    }


}


print(f'3. Students: {student}')



# 4


print(f'4. Dictionary length: {len(student)}')


# 5

print(f'5. Skills: {student["skills"]}\n   Data Type: {type(student["skills"])}')

# 6
student["skills"].append('Motivational Speaking')

print(f'6. Skills: {student["skills"]}')

# 7
student_keys = student.keys()
print(f'7. Keys: {student_keys}')

# 8
student_values = student.values()
print(f'8. Values: {student_values}')

# 9
it = student.items()
for i in it:
    print(f'{i}\n')
  
print(f'9. Using items() method: {None}')

# 10

# popped_item = student.pop('age')
popped_item = student.popitem()
# del student['age']
print(f'10. Student: {student} \n   Popped item: {popped_item}')

# 11

del student

# print(len(dog))
