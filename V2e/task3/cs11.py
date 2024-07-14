data = [('Reny',19,95,80,'F'),('John',20,105,90,'M'),('Jony',17,81,91,'M'),('Jony',17,70,93,'M'),('Json',21,65,85,'F'),('Angel',19,59,79,'F')]


# data = [(name, age, weight, height, gender, int(weight / ((height / 100) ** 2))) for name, age, weight, height, gender in data]
newdata  = []
for name, age, weight, height, gender in data:
    tup = (name, age, weight, height, gender, int(weight / ((height / 100) ** 2)))
    newdata.append(tup) 

sorted_data = sorted(newdata, key=lambda x: (x[4], x[0], x[1], x[5]))

for i in sorted_data:
    print(i)