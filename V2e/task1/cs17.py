class Number:
    
    def calc(self,inp):
        string=inp.split()
        print(type(string))
        tcount=0
        lword = ""
        for words in string:
            tcount+=len(words)
            if(len(words)>len(lword)):
                lword = words
        print("length: ",tcount)
        print(lword)
        print(len(lword))
        div = str(tcount//len(lword))
        return div
    
    def convert(self):
        div = o1.calc(inp)
        print(div)
        alp = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',0:'J'}
        for i in div:
            print(alp[int(i)],end='')
        
inp = input("Enter: ")
o1=Number()
o1.convert()
