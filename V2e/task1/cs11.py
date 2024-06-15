class Solution:
    
    def solve(self,str1,str2):
        
        print(str1,'\n',str2)
        d1={}
        d2={}


        for ch in str1:
            if(ch in d1):
                d1[ch]+=1
            else:
                d1[ch] = 1
        print(d1)

        for ch in str2:
            if(ch in d2):
                d2[ch]+=1
            else:
                d2[ch] = 1
        print(d2)

        str1=list(str1)
        str2=list(str2)
        d = d1.__reversed__()
        d3 = d2.__reversed__()

        for i in d:
            a = d1[i]
            str2[a]=i
        for k in d3:
            a = d2[k]
            str1[a]=k

        print(*str1,'\n',*str2)
        
        
str1 = 'asdfds'
str2 = 'sdgdrw'
o1=Solution()
o1.solve(str1,str2)
    