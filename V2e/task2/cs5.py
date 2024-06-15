class String:
          
    def order_str(self,string=''):
         
        lowerCase,upperCase = "",""
        for i in string:
            if i.islower():
                lowerCase+=i
            elif i.isupper():
                upperCase+=i
        print(lowerCase+upperCase)
    
string = input()
object1 = String()
object1.order_str()