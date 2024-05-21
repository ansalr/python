# l = []
# nl = int(input("Number of list : "))
# for i in range(nl):
#     n = list(map(int, input().split()))
#     l+=[n]


l = [[27,9,2,8,8,9,27,8],[1,18,2,1,18,4,4,6],[1,5,7,5,8,7,4,5],[1,2,3,5,8,4,4,3]]
d={}
cc = 0
al = 97
print(cc)
sum = 1
h=0
for i in range(len(l)):
    
    for j in range(len(l[i])):
        c = l[i].count((l[i][j]))
        if c == 1:
            sum*=(i+1)
            
            if cc == 0:
                d[i+1]=l[i][j]
                # lc+=1
            elif cc > 0:
                d[str(i+1)+chr(al)]=l[i][j]
                # cc+=1
                al+=1
            cc+=1
    cc = 0
    lc = 0
    al = 97

print(d)
print(sum)



            

