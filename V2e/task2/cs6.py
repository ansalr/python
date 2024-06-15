class Numbers:
    
    def calc(self,string):
        letter = 0
        number = 0
        special = 0
        for i in string:
            if i.isalpha():
                letter+=1
            elif i.isdigit():
                number+=1
            else:
                special+=1
        product = str(letter*number*special)
        print(product)
        alp1 = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',0:'J'}
        
        for i in product:
            print(str(i),'-',alp1[int(i)])   
       
string  = input("enter string: ")       
object1 = Numbers()
object1.calc(string)
             