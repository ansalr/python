class String:
    
    def get_input(self):
        stringList = input().split()
        return stringList
        
    def newList(self,stringList):
        outputList = []
        for string in stringList:
            for ch in string:
                if ch.isdigit():
                    outputList.append(string)
                    break
        return outputList
    
    def alpPosition(self,outputList):
        d = {}
        product = 1
        for string in outputList:
            for ch in string:
                if ch.isalpha():
                    num = (ord(ch.lower()))-96
                    product*=num
                
                if ch.isdigit():
                    product *=int(ch)
            d[string] = product
        return d                  
                
    def print_output(self):
        stringList = self.get_input()
        outputList = self.newList(stringList)
        print(outputList)
        output = self.alpPosition(outputList)
        print(output)
               
      
object1 = String()
object1.print_output() 