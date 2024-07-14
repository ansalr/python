class Exercise8:
    
    def solution(self):
        
        data = "Helloall!!WelcometoV2etechnologies--Holatodas!!bienvenidoV2etechnologies."
        newdata = []
        newdata1 = []
        string = ''
        start = 0

        for i in range(9):
            newdata.append(data[start:start+8])
            start +=8
        print(newdata)
        for i in range(8):
            string = ''
            for value in newdata:
                letter = value[i]
            
                string += letter
            newdata1.append(string)
        print(newdata1)

        newdic = {}  
        for i in range(len(newdata1)):
            splitdata = list(newdata1[i])
            count = 0
            for j in splitdata:
                if j.lower() in ['a','e','i','o','u']:
                    count+=1
            newdic[i]= count
            
        print(newdic)
        
object1 = Exercise8()
object1.solution()