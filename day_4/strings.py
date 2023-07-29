## Exercises Day 4

# 1
string = 'Fifteen' + 'Days' + 'Of' + 'Smiling'

# 2
string2 = 'Coding' + 'For' + 'All'

# 3
company = string2

# 4
print(f'4. {company}')

# 5
print(f'5. {len(company)}')

# 6
print(f'6. {company.upper()}')

# 7
print(f'7. {company.lower()}')

# 8
print(f'8. {"Coding For All".capitalize()}')
print(f'   {"Coding For All".title()}')
print(f'   {"Coding For All".swapcase()}')

# 9
print(f'9. {"Coding For All"[6:]}')
# print(f'9. {"Coding For All".removeprefix("Coding")}')

# 10
print(f'10. {"Coding For All".index("Coding")}')

# 11
print(f'11. {"Coding For All".replace("Coding", "Python")}')

# 12
print(f'12. {"Python For Everyone".replace("Everyone", "All")}')

# 13
print(f'13. {"Coding For All".split(" ")}')

# 14
print(f'14. {"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(", ")}')

# 15
print(f'15. {"Coding For All"[0]}')

# 16
# print(f'16. {len("Coding For All") - 1}')
print(f'16. {"Coding For All".rfind("l")}')

# 17
print(f'17. {"Coding For All"[10]}')

# 18
print(f'18.\t{"Python For Everyone"}')
#----------------------------------------------------------------

# 19
print(f'19.\t{"Coding For All"}')

# 20
print(f'20. {"Coding For All".index("C")}')

# 21
print(f'21. {"Coding For All".index("F")}')

# 22
print(f'22. {"Coding For All".rfind("l")}')

# 23
print(f'23. {"You cannot end a sentence with because because because is a conjunction".find("because")}')

# 24
print(f'24. {"You cannot end a sentence with because because is a conjunction".rindex("because")}')

# 25
phrase = "You cannot end a sentence with because because because is a conjunction"
phrase.strip('because')
print(f'25. {phrase.replace("because ", "")}')

# 26
print(f'26. {"You cannot end a sentence with because because because is a conjunction".index("because")}')
