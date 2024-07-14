# inputLength = int(input("Enter length : "))
# data = []
data = [('Reny',19,80,'F'),('John',20,90,'M'),('Jony', 17, 91,'M'),('Jony', 17, 93,'M'),('Reny',28,85,'F'),('Jason',21,85,'F'),('Angel',19,79,'F')]
# for _ in range(inputLength):
#     name, age, height, Gender = input().split(',')
#     age = int(age)
#     height = int(height)
#     inputTuple = [name, age, height, Gender]
#     data.append(tuple(inputTuple))

sorted_data = sorted(data, key=lambda x: (x[3], x[0], x[1], x[2]))
for i in sorted_data:
    print(i)