class Solution:
    def __init__(self) -> None:
        self.matrix = []
          
    def print_matrix(self):
        print("----Matrix----")
        for i in self.matrix:
                print(i)
        
    def validate_matrix(self,size):
        if size%2 == 0:
            for i in range(1,size+1):
                nl=[]
                for j in range(size):
                    num = str(input("value: "))
                    nl.append(num)
                self.matrix.append(nl)
            object1.print_matrix()
            alp = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22,'w': 23, 'x': 24, 'y': 25,'z': 26}
            print("Even Matrix: ")
            for i in range(1,len(self.matrix)+1):
                if i%2==0:
                    print(self.matrix[i-1])
                    for j,k in  enumerate(self.matrix[i-1]):
                        self.matrix[i-1][j]=alp[k]
                else:
                    for j,k in  enumerate(self.matrix[i-1]):
                        self.matrix[i-1][j]=alp[k]
            print("************************")
            for i in range(int(len(self.matrix)/2)):
                for j,k in zip(self.matrix[i],self.matrix[i+1]):
                    if j%k ==0:
                        j,k=k,j
            object1.print_matrix()
            
        else:
            print("Only even number accept")
            object1.get_input()
            
    def get_input(self):
        size = int(input("Matrix size: "))
        object1.validate_matrix(size) 
        
object1=Solution()
object1.get_input()

