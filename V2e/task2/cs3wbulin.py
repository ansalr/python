class Findstring:
    
    def convertstr(self):
        string = "hello how are you"
        inputString = input()
        count = string.count(inputString)
        newString = string.replace(inputString,str(count),count)
        print(newString)
        return newString
    
    def removeWord(self):
        String = self.convertstr()
        newString = String.split()
        word = input()
        if word not in newString:
            print("Word not found")
        else:
            print(String.replace(word, str(len(word))))
            
             
    
object1 = Findstring()
object1.removeWord()