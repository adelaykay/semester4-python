# Level 2
siblings1 = ('Segun', 'Dayo', 'Bisi', 'Ronke', 'Bimbo', 'Naomi')
parents1 = ('Emmanuel', 'Judith')
family_members = siblings1 + parents1

# 1
*siblings, p1, p2 = family_members
s1,s2,s3,s4,s5,s6,*parents = family_members
print(f'1. Siblings: {siblings}\n   Parents: {parents}')

# 2
fruits, vegetables, animal_products = ('apple', 'orange', 'okro'), ('carrot', 'lettuce')\
  , ('milk', 'fish', 'beef')

food_stuff_tp = fruits + vegetables + animal_products

print(f'2. Food Stuff: {food_stuff_tp}')

# 3
food_stuff_lt = list(food_stuff_tp)

print(f'3. Food Stuff: {food_stuff_lt}')

# 4

middle_item = food_stuff_lt[len(food_stuff_lt) // 2]
print(f'4. Middle Item: {middle_item}')
