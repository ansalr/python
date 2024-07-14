class Utility:
    
    def __init__(self):
        self.inputlist = []
        
    def get_input(self):
    
        try:
            while True:
                user_input = input("Enter a tuple (name, age, weight, height, gender) or press Enter to stop: ")
                if not user_input:
                    break
                name, age, weight, height, gender = user_input.split(',')
                # print((name, age, int(int(weight) / ((int(height) / 100) ** 2)), gender))
                self.inputlist.append((name, age, int(int(weight) / ((int(height) / 100) ** 2)), gender))
        except ValueError:
            print("Input name,age,height should be seperated by comma")
        return self.inputlist

class Exercise11(Utility):
           
    def arrange(self):
        tuples = super().get_input()
        print(tuples)
        n = len(tuples)

        for i in range(n):
            for j in range(0, n - i - 1):
                try:
                    if self.compare(tuples[j], tuples[j + 1]) > 0:
                        tuples[j], tuples[j + 1] = tuples[j + 1], tuples[j]
                except TypeError:
                    ...
        
        
        print(tuples)
        
    def compare(self,t1,t2):
        presidence = [3, 0, 1, 2]
        for i in range(len(presidence)-1):
            if t1[presidence[i]] != t2[presidence[i]]:
                print(t1[presidence[i]],t2[presidence[i]])
                return 1 if t1[presidence[i]] > t2[presidence[i]] else -1
            else:
                continue
       
object1= Exercise11()
object1.arrange()

"""
Reny,19,95,80,F
John,20,105,90,M
Jony,17,81,91,M
Jony,17,70,93,M
Json,21,65,85,F
Angel,19,59,79,F
"""