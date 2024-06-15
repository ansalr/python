class Numbers:
    def __init__(self) -> None:
        self.string = ''
        self.string1 = None
        self.string2 = None
    
    def get_input(self):
        string1 = input()
        string2 = input()
        if len(string1) >= 3 and len(string2)>=3:
            return string1,string2
        else:
            return
        
    def first_letter(self,string1,string2):
        self.string += string1[0]+string2[0]
    
    def middle_letter(self,string1,string2):
        
        mid1 = int(len(string1)/2)
        mid2 = int(len(string2)/2)
        self.string += string1[mid1]+ string2[mid2]
        # print(self.string)
        
    def end_letter(self,string1,string2):
        self.string += string1[-1]+string2[-1] 
        
    def print_string(self):
        try:
            a,b = object1.get_input()
            self.first_letter(a,b)
            self.middle_letter(a,b)
            self.end_letter(a,b)
            print(self.string)
        
        except TypeError:
            print("Both input length must be greater than or equal to 3")    

   
object1 = Numbers()
object1.print_string()