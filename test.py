# class A:
#     def __init__(self) -> None:
#         print('A')
#         pass

# class B():
#     def __init__(self) -> None:
#         super().__init__()
#         print("B")
#         pass

# class c(B,A):
#     def __init__(self) -> None:
#         super(c,self).__init__()
#         print("C")
# obj1 = c()
# print(obj1)

# class student:
#     def __init__(self,name,age) -> None:
#         assert age >5,f"age should be greater than 5"
#         self.name = name
#         self.age = age
#         pass

#     @classmethod
#     def print_name(cls):
#         print("hellow")

#     @staticmethod
#     def isfloat(num):

#         if isinstance(num,float):
#             return num.is_integer()
#         elif isinstance(num,int):
#             return True
#         else:
#             return False
        
#     def function(self):
#         print(f"{type(self).__name__}")
        


# print(student.isfloat(22))
# obj1 = student("ansal",12) 
# obj1.function()


# import random
# names = ["Jacob", "Joe", "Jim"]
# print(random.random())
# print(random.choice(names))
# print(random.randint(1,10))
# print(random.randrange(0,20,2))


# names = ["Jacob", "Joe", "Jim"]

# if (name := input("Enter your Name: ")) in names:
#     print(f"Hellow {name}")
# else:
#     print(f"name not Found")

# num_list = [i for i in range(1,5)]
# print(num_list)

# s = open('python.txt').read()
# print(s)


