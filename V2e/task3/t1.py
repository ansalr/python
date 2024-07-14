class Utility:    
    def __init__(self):
        self.inputlist = []
        
    def get_input(self):    
        try:
            while True:
                user_input = input("Enter a tuple (name,age,height) or press Enter to stop: ")
                if not user_input:
                    break
                name, age, height = user_input.split(',')
                print((name, age, height))
                self.inputlist.append((name, age, height))
        except ValueError:
            print("Input name,age,height should be seperated by comma")        

class Exercise2(Utility):
    def __init__(self):
        super().__init__()
        self.get_input()
    
    def arrange(self):
        print(self.inputlist)
        for i in range(len(self.inputlist)):
            for j in range(0, len(self.inputlist) - i - 1):
                if self.compare(self.inputlist[j], self.inputlist[j + 1]) > 0:
                    self.inputlist[j], self.inputlist[j + 1] = self.inputlist[j + 1], self.inputlist[j]
        
    def compare(self,t1,t2):
        presidence = [0,1,2]
        for i in range(len(presidence)-1):
            if t1[presidence[i]] != t2[presidence[i]]:
                return 1 if t1[presidence[i]] > t2[presidence[i]] else -1
            else:continue
        return 0
                
       
object1= Exercise2()
object1.arrange()