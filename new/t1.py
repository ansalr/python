n = [("Reny",19,80,'F'),("John",20,90,'M'), ("John",17, 91,'M'),("John",17,93,'M'),("Reny",28,85,'F'),("jason",21,85,'M'),("Angel",19,79,'F')]
# sort priority  n[3]>n[0]>n[1]>n[2]
# n = input()
# print (type(n))
fc=0
new = []
name = []
for i in range(len(n)):
    sname=n[i][0]    
    name+=[sname]
    if n[i][3] == 'F':
        new.insert(0,n[i])
        fc+=1
    elif n[i][3] =='M':
        new.append(n[i])

print(new)
print(fc)


