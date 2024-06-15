class Number:
    
    def get_input(self):
        string1 = input()
        string2 = input()
        return string1,string2
    
    def balance(self,string1,string2):
        for i in string1:
            if i not in string2:
                print("Not balance String")
                return 0
            return 1
               
    def construct_string(self,string1,string2):
        newString = ''
        if len(string1) > len(string2):
            length = len(string2)
            maxlen = len(string1)
            max = 0
        elif (len(string2)> len(string1)):
            length = len(string1)
            maxlen = len(string2)
            max = 1
        for i in range(length):
            newString+=string1[i]+string2[-(i+1)]
        
        if max == 0:
            
            newString += string1[length:]
        else:  
            remain = maxlen-length
            newString += string2[:remain]
        return newString
            
         
    def get_output(self):
        
               
        s1,s2 = self.get_input()
        n = self.balance(s1,s2)
        if n:
            output = self.construct_string(s1,s2)
            print(output)
        
    
    

object1 = Number()
object1.get_output()