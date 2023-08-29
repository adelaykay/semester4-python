'''
Python Dictionaries
'''

empty_dict = {}

person = {
  'first_name': 'Adeleke',
  'last_name': 'Olaolu',
  'middle_name': 'Olasope',
  'country': 'Nigeria',
  'skills': ['Programming', 'Music', 'Entertainment'],
  'address': {
    'street': '45, Awolowo Avenue',
    'zipcode': 101282
    }
  }

person['phone'] = '2348136623644'
person[100]= 'age'  # add item
groceries = person.fromkeys(person, '')
print(groceries)
# person.pop('middle_name')  # removes the last added pair
# popped_item = person.popitem()  # removes the last added pair and returns them as tuple
# del person['middle_name']  # deletes the pair whose key is given
person_keys = person.keys()  # returns a list of all the key in the person dictionary
person_values = person.values()  # returns a list of all the values in the person dictionary

# print(100 in person)
# print(popped_item)
# print(person_keys)
# print(person_values)
# print(person)
