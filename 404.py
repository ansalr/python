# print number
print(8)

# print string
print("i am human")

# print variable using format string
name = "Ansal"
species = "human"
print(f"i am human {name}")

# named placeholder
print("my name is {} \n i am {}".format(name,species))

# numbered placeholder
print("my name is {1} \ni am {1}".format(species,name))

# empty placeholder 
print("my name is {1} \ni am {1}".format(species,name))

# Arithmetic Operations
a = 4
b = 2

# Addition
print(f"sum : {a+b}")

# subraction
print(a-b)

# Division
print(a/b)

# multiplication
print(a*b)

# Exponential
print(a**b)

# reminder
print(a%b)

# quotient
print(a//b)

# Concatenation
x = "Good"
y = "Work"
print(x + y)
print(x + " " + y)

# Numeric variables - hold integers and decimal values
age = 25
temperature = 98.6

# String variables - Stores a sequence of characters enclosed in single or double quotes
name = "John Doe"
message = 'Hello, world!'

# Boolean variables - only hold the values true and false
is_true = True
is_false = False

# List variables - Stores a collection of items, which can be of different types.
numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'orange']


string = [C ,o ,d ,e ,C ,h ,e ,f]
"""
 0 1 2 3 4 5 6 7  - index number
"C o d e C h e f"

"""

# Tuple variables
coordinates = (10, 20)

# Dictionary variables
person = {'name': 'Alice', 'age': 30}

# Set variables
unique_numbers = {1, 2, 3}

# None variable
empty_value = None

# command to accept user input from the console
name = input()       
print("Your name is:", name)

name = input("Enter your name: ")
print("Hello, " + name + "!")

age = input("Enter your age: ")
print("You are " + age + " years old.")

age = int(input())
print("You are", age, "years old.")