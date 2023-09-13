num = 2

if num > 0:
    if num % 2 == 0:
        print("A is a positive and even integer")
    else:
        print("A is a positive number")
elif num == 0:
    print("A is zero")
else:
    print("A is a negative number")
    
    
a = 0
if a > 0 and a % 2 == 0:
    print("A is an even and positive integer")
elif a > 0 and a % 2 != 0:
    print("A is a positive odd integer")
elif a == 0:
    print("A is zero")
else:
    print("A is a negative number")

user = 'student'
access_level = 3

if user == 'admin' or access_level >= 4:
    print("Access granted")
else:
    print("Access Denied")

