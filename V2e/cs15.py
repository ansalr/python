class Premide:
    def __init__(self) -> None:
        self.num = 49
        self.l = 64
        
    def digram(self,n):
        for i in range(n+1):
            letter = chr(self.l)
            print(letter*i)
            self.l+=1
        while(i>0):
            print(str(i)*i)
            i-=1
            
n = 5
o1=Premide()
o1.digram(n)








# n = 5
# num = 49
# l = 64
# for i in range(n+1):
#     letter = chr(l)
#     print(letter*i)
#     l+=1
# while(i>0):
#     print(str(i)*i)
#     i-=1