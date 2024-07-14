class Robot:
    
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        
    def calculate(self,movements):
        for move in movements:
            if move[0].upper() == "UP":
                self.y += move[1]
            elif move[0].upper() == "DOWN":
                self.y -= move[1]
            elif move[0].upper() == "LEFT":
                self.x -= move[1]
            elif move[0].upper() == "RIGHT":
                self.x += move[1]

        if self.x < 0:
            print("Right: ",0,"\nLeft: ",abs(self.x))
        else:
            print("Right: ",abs(self.x),"\nLeft: ",0)
            
        if self.y < 0:
            print("Down: ",0,"\nUP: ",abs(self.y))
        else:
            print("Down: ",0,"\nUP: ",abs(self.y))
            
        
        
        
        

# movements = [("up", 5), ("DOWN", 3), ("LEFT", 3), ("RIGHT", 2),("up", 6),("RIGHT", 3),("DOWN", 1)]
movements = [("up", 5), ("DOWN", 3), ("LEFT", 3), ("RIGHT", 2)]
object1 = Robot()
object1.calculate(movements)




