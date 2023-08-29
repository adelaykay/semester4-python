'''
Exercises - Day 7
'''

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
numbers_a = {19, 22,24,20,25,26}
numbers_b = {19, 22,20,25,26,24,28,27}
ages = [22, 19, 24, 25, 26, 24, 25, 24]

# Level 1
print('Level 1')
# 1
print(f'1. Length of IT companies set: {len(it_companies)}')

# 2
it_companies.add('Twitter')
print(f'2. IT companies set: {it_companies}')

# 3
it_companies.update(['Youtube', 'Netflix', 'WhatsApp'])
print(f'3. IT companies set: {it_companies}')

# 4
it_companies.remove('Twitter')
print(f'4. IT companies set: {it_companies}')

# 5
it_companies.discard('Telegram')
# it_companies.remove('Twitter')

# Level 2
print('\nLevel 2')
# 1
print(f'1. Join numbers A and B: {numbers_a.union(numbers_b)}')

# 2
print(f'2. A intersection B: {numbers_a.intersection(numbers_b)}')

# 3
print(f'3. Is A subset of B: {numbers_a.issubset(numbers_b)}')

# 4
print(f'4. Are A and B disjoint: {numbers_a.isdisjoint(numbers_b)}')

# 5
print(f'5. ')

# 6
print(f'6. Symmetric difference between A and B: {numbers_a.symmetric_difference(numbers_b)}')

# 7
del it_companies
del numbers_a
del numbers_b
# del age
# print(f'7. it_companies: {it_companies}, A: {numbers_a}, B: {numbers_b}, age: {age}')

# Level 3
print('\nLevel 3')
# 1
ages_set = set(ages)
print(f'1. age list length: {len(ages)}, ages set length: {len(ages_set)}')

# 2
print('''
2. Explain the difference between strings, lists, tuples and sets
-----------------------------------------------------------------
Lists are an ordered collection of mutable elements. Elements may include any data type.
Tuples are an ordered collection of immutable elements.
Strings are an immutable sequence of characters.
Sets are an unordered collection of unique elements. Sets are mutable.
''')

# 3
sentence = 'I am a teacher and I love to inspire and teach people'
sentence = set(sentence.split(' '))
print(f'3. Unique words: {sentence}, Number of unique words: {len(sentence)}')