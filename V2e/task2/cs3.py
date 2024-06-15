class Findstring:
   
    def convertstr(self):
        string = "hello how are you"
        print(string)
        inputString = input()
        countdict = {}
        for ch in string:
            if ch not in countdict:
                countdict[ch] = 1
            else:
                countdict[ch] +=1
        count = countdict[inputString]
        print(count)
        
        newString = ''
        for ch in string:
            if ch == inputString:
                newString += str(count)
            else:
                newString +=ch
                
        print(newString)
        return newString
    
    def removeWord(self):
        String = self.convertstr()
        newlist = []
        newword = ''
        for i in String:
            if i == ' ':
                newlist.append(newword)
                newword = ''
                newlist.append(' ')

            else:
                newword += i
                
        word = input()
        if word not in newlist:
            print("Word not found")
        else:
            print(String.replace(word, str(len(word))))
            
                 
object1 = Findstring()
object1.removeWord()
