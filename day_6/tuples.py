'''

TUPLES
'''

# Level 1


# 1 - Create an empty tuple

empty_tuple = ()

print(f'1. Empty tuple: {empty_tuple}')


# 2 - Create a tuple containing names of your sisters and brothers

brothers = ('Segun', 'Dayo')

sisters = ('Bisi', 'Ronke', 'Bimbo','Naomi')

print(f'2. Sisters: {sisters}\n   Brothers: {brothers}')


# 3 - Join the brothers and sisters tuples together

siblings = brothers + sisters

print(f'3. Siblings: {siblings}')


# 4 - How many siblings are there?

print(f'4. Number of siblings: {len(siblings)}')


# 5 -Modify the siblings tuple by adding the names of your father and mother

family_members = siblings + ('Emmanuel', 'Judith')

print(f'5. Family members: {family_members}')


# Level 2


# 1 - Unpack siblings and parents from family members

(*siblings, father, mother), (a,b,c,d,e,f,*parents)= family_members, family_members

print(f'1. Siblings: {siblings}\n   Parents: {parents}')


# 2 - Create fruits, vegetables and animal products tuples

#     Join the three tuples and assign to food_stuff_tp

fruits, vegetables, animal_products = ('apple', 'orange', 'okro'), ('broccoli', 'carrots')\
  ,('milk', 'beef', 'fish')

food_stuff_tp = fruits + vegetables + animal_products

print(f'2. Food Stuff: {food_stuff_tp}')


# 3 - Change the food_stuff_tp tuple to a list

food_stuff_lt = list(food_stuff_tp)

print(f'3. Food Stuff: {food_stuff_lt}')


# 4 - Slice out the middle item from the food_stuff_tp

MIDDLE_ITEM = food_stuff_tp[len(food_stuff_tp)//2]
print(f'4. Middle Item: {MIDDLE_ITEM}')

# 5 - Slice out the first three items and last three items from the food stuff list

first_three, last_three = food_stuff_tp[:3], food_stuff_tp[-3:]
print(f'5. First three items: {first_three}\n   Last three items: {last_three}')

# 6 - Delete the food stuff tuple completely
del food_stuff_tp
# print(f'6. Food Stuff: {food_stuff_tp}')

# 7 - Check if an item exists in tuple
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print(f'7. {"Estonia" in nordic_countries}\n   {"Iceland" in nordic_countries}')
