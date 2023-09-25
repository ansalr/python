# print(f"{(lambda a,b:a*b)(4,3)}")
# Python program to
# demonstrate protected members

# Python program to
# demonstrate private members

# Creating a Derived class


class Base:
	def __init__(self):
		self.a = "Geeks"
		self.__c = "GeeksforGeeks"
		print(self.__c)

# Creating a derived class
class Derived(Base):
	def __init__(self):

		# Calling constructor of
		# Base class
		Base.__init__(self)
		print("Calling private member of base class: ")
		print(self.__c)


# Driver code
Derived()
# print(Base())

# Uncommenting print(obj1.c) will
# raise an AttributeError

# Uncommenting obj2 = Derived() will
# also raise an AttributeError as
# private member of base class
# is called inside derived class










"""import datetime as datetime
today = datetime.datetime.now()
print(today.day)
print(today.month)
print(today.year)
print(today.hour-12)
print(today.minute)
print(today.second)"""