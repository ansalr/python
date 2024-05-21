# inp = list(map(str,input().split(',')))
# nlist=[]
# for i in range(1,len(inp),2):
#     nlist.append(inp[i])
# print(nlist)


# inp_list=['one','two','three','four','five','six','seven','eight','nine','ten']
# one,two,three,four,five,six,seven,eight,nine,ten
# inp_list=list(map(str,input().split()))

# new_d={}
# for i in range(0,int(len(inp)/2),2):
#     new_d[inp[i]]=inp[i+1]
    
# print(new_d)

class Number:
    def __init__(self) -> None:
        self.nlist=[]
        self.new_d={}
        
    def calc(self,inp):
        for i in range(1,len(inp),2):
            self.nlist.append(inp[i])
        print(self.nlist)
        
        for i in range(0,int(len(inp)/2),2):
            self.new_d[inp[i]]=inp[i+1]
            
        print(self.new_d)
                
        
inp = list(map(str,input().split(',')))
o1=Number()
o1.calc(inp)