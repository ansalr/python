class Number:
    
    def cal(self,n):
        print(1)
        for i in range(1,n):
            print(2,end=' ')
            a  = 6
            p = 2
            for j in range (i):
                sum = p+a
                print(sum,end=' ')
                p = sum
                a +=4
            print()
        i =n
        while(i > 0):
            m = 0 
            i-=1
            for l in range(i):
                print((m**2)+m,end=' ')
                m+=1
            print()

n = 5
o1 = Number()
o1.cal(n)    













# n = 5
# print(1)
# for i in range(1,n):
#     print(2,end=' ')
#     a  = 6
#     p = 2
#     for j in range (i):
#         sum = p+a
#         print(sum,end=' ')
#         p = sum
#         a +=4
#     print()
# i =n
# while(i > 0):
#     m = 0 
#     i-=1
#     for l in range(i):
#         print((m**2)+m,end=' ')
#         m+=1
#     print()
    