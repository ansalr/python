class Number:
            
    def calc(self,l):
        d = {}
        for i in range(len(l)):
            if l[i]>=104 and l[i]<=168:
                if l[i]%13==0:
                    if l[i]%2 ==0:
                        
                        d[str(l[i-1])] = l[i]*2
                    else:
                        d[str(l[i-1])] = l[i]*3
        print(d)
        
l = [150,145,130,120,143,156,125]
o1=Number()
o1.calc(l)













# l = [150,145,130,120,143,156,125]
# d = {}
# for i in range(len(l)):
#     if l[i]>=104 and l[i]<=168:
#         if l[i]%13==0:
#             if l[i]%2 ==0:
                
#                 d[str(l[i-1])] = l[i]*2
#             else:
#                 d[str(l[i-1])] = l[i]*3
# print(d)