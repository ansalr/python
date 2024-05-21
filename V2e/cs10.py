class Number:
    
    def calc(self,inp):
        
        spl = "{}[];':\",.<>?!@#$/\\"
        alp = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22,'w': 23, 'x': 24, 'y': 25,'z': 26}
        alp1 = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',0:'J'}
        al = 0
        nums = 1
        for char in inp:
            if char in alp:
                al+=alp[char]
            elif(char.isnumeric()):
                nums*=int(char)
            elif(char in spl):
                continue
        result = str(al)+str(nums)
        print(result)

        for i in result:
            print(i,"-",alp1[int(i)])


inp = str(input("enter string: "))
o1=Number()
o1.calc(inp)