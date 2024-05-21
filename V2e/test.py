import re
# n= "ad768D&"
n = input("Enter string: ")
pattern = re.compile('''^(?=.*[a-z]{2,5})(?=.*[0-9]{3,4})(?=.*[A-Z]{1,2})(?=.*[!@#$%^&*]{1,2}).{5,10}$''')

if pattern.match(n):
    print("Valid")
else:
    print("not valid")