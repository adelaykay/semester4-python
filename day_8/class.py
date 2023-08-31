'''
dict
'''

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

student_keys = student.keys()
student_keys_list = list(student.keys())

print(student_keys_list, type(student_keys_list))
