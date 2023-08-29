'''
'''

# fruits = {'orange', 'lemon', 'apple'}
# veggies = {'lettuce', 'carrot'}
# fruits.add('okro')
# fruits.update(['okro', 'grape'])
# popped_item = fruits.pop()
# fruits.pop('okro')
# fruits.remove('apple')
# fruits.clear()
# fruits_list = list(fruits)
# fruits_set = set(fruits_list)
# joined_set = fruits.union(veggies)
# intersect = fruits.intersection(joined_set)
# print(intersect)


whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
is_subset = even_numbers.issubset(whole_numbers)
is_superset = whole_numbers.issuperset(even_numbers)
odd_numbers = whole_numbers.difference(even_numbers)
is_disjoint = odd_numbers.isdisjoint(even_numbers)
print()
