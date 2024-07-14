class Dictionary:

    def createDictionary(self,n):
        
        integral = {}
        for i in range(1,n+1):
            
            integral[i] = i*i
        print(integral)

        
inputnum = int(input("Enter Number :"))
instance1 = Dictionary()
instance1.createDictionary(inputnum)