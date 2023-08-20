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
firstCompany = it_companies[0]
middleCompany = it_companies[len(it_companies)//2]
lastCompany = it_companies[len(it_companies)-1]
print(f'9. First company: {firstCompany}, middle company: {middleCompany}, last company: {lastCompany}')

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
print(f'16. IT companies {it_companies}')

