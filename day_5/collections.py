## Exercises Day 5

# 1

emptyList = []

print(f'1. {emptyList}')

# 2

sixItemList = [0, True, 2.0, 'False', [], {1: True, 2: False}]

print(f'2. {sixItemList}')


# 3

lengthOfList = len(sixItemList)

print(f'3. Length of my list: {lengthOfList}')


# 4

firstItem = sixItemList[0]

middleItem = sixItemList[3]

lastItem = sixItemList[lengthOfList - 1]

print(f'4. First item: {firstItem}, middle item: {middleItem} and last item: {lastItem}')


# 5

mixed_data_types = ['Adeleke', 34, 1.79, 'single', '1600 Pennsylvania Avenue NW']

print(f'5. Mixed data types: {mixed_data_types}')


# 6

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print(f'6. IT companies: {it_companies}')


# 7

print(f'7. IT companies: {it_companies}')


# 8

print(f'8. Number of IT companies: {len(it_companies)}')


# 9
FIRST_COMPANY = it_companies[0]

middleCompany = it_companies[len(it_companies)//2]

lastCompany = it_companies[len(it_companies)-1]

print(f'9. First company: {FIRST_COMPANY}, middle company: {middleCompany},\
  last company: {lastCompany}')


# 10

it_companies[0] = 'Twitter'

print(f'10. IT companies: {it_companies}')

# 11

it_companies.append('Facebook')

print(f'11. IT companies: {it_companies}')

# 12

it_companies.insert(len(it_companies)//2, 'Samsung')

print(f'12. IT companies: {it_companies}')


# 13

it_companies[0] = it_companies[0].upper()

print(f'13. IT companies: {it_companies}')


# 14

joined = it_companies.extend("#; ")

print(f'14. {joined}')


# 15

print(f'15. {"Google" in it_companies}')


# 16
it_companies.sort()

print(f'16. IT companies: {it_companies}')


# 17

it_companies.reverse()

print(f'17. IT companies: {it_companies}')


# 18

sliceFirstThree = it_companies[0:3]

print(f'18. slice: {sliceFirstThree}')


# 19

sliceLastThree = it_companies[-3:]

print(f'19. slice: {sliceLastThree}')


# 20

sliceMiddle = it_companies[len(it_companies)//2]

print(f'20. slice: {sliceMiddle}')

# 21

it_companies.pop(0)
print(f'21. it_companies: {it_companies}')

# 22

it_companies.pop(len(it_companies)//2)
print(f'22. it_companies: {it_companies}')


# 23
it_companies.pop()

print(f'23. it_companies: {it_companies}')


# 24
it_companies.clear()

print(f'24. it_companies: {it_companies}')


# 25



# 26 27

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']

back_end = ['Node', 'Express', 'MongoDB']

joinedList = front_end + back_end

print(f'27. Frontend + Backend: {joinedList}')


# 28

full_stack = joinedList.copy()

full_stack.insert(5, ['Python', 'SQL'])

print(f'28. Full Stack: {full_stack}')


# Level 2
# 1

ages = [19,22,19,24,20,25,26,24,25,24]
#######
ages.sort()
print(f'1. ages: {ages}')
#######

min_age = ages[0]

print(f' Minimum age: {min_age}')
#######

max_age = ages[-1]

print(f' Maximum age: {max_age}')
#######

median_age = ages[len(ages)//2]

print(f' Median age: {median_age}')
#######

average_age = sum(ages)/len(ages)

print(f' Average age: {average_age}')
#######

print(f' Range of ages: {ages[-1] - ages[0]}')
#######


# 2

# Find the middle country in the middle of a country list

countries = ['Egypt', 'Albania', 'Algeria', 'USA', \

  'Colombia', 'Bolivia', 'Uruguay', 'India', 'Maldives', 'Qatar']

print(f'2. Middle country: {countries[len(countries) // 2]}')


# 3

# Divide the countries list into two equally sized lists

countries_a = countries[0:len(countries) // 2]

countries_b = countries[len(countries) // 2:]

