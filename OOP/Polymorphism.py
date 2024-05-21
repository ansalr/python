class Animal:
    def __init__ (self, name,age):
        self.name = name
        self.age = age

class Dog(Animal):
    def __init__(self, name, age,breed):
        super().__init__(name, age)
        self.breed = breed
    
    def fetch(self,breed):
        print(f"name: {self.name} \nAge: {self.age}\n Breed: {self.breed}")
a = Animal("Yommy",2)
a.

#     def eat(self, food):
#         print ( "{0} eats {1}".format(self.name, food))

# class Dog(Animal):
#     def fetch(self, thing):
#         print( "{0} goes after the {1}!".format(self.name, thing))
#     def show_affection(self):
#         print("{0} wags tail".format(self.name))

# class Cat(Animal):
#     def swatstring(self):
#         print("{0} shreds the string!".format(self.name))
#     def show_affection(self):
#         print("{0} purrs".format(self.name))

# for a in ( Dog( 'Rover'), Cat('F1uffy'), Cat('precious' ), Dog('Scout')):
#     a.show_affection()
