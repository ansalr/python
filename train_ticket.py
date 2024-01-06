class ticket:
    def __init__(self) -> None:
        self.u = 21
        self.m = 21
        self.l = 21
        self.rac = 18
        self.wait = 10
        self.id = 0
        
        

    def print_tick(self,birth = None):
        if birth == 'u':
            self.u -=1
        elif birth == 'm':
            self.m -=1
        elif birth == 'l':
            self.l -=1
        elif birth == 'rac':
            self.rac -=1
        elif birth == "wait":
            self.wait -=1

        print(f"Available ticket :")
        print(f"upper        : {self.u}")
        print(f"Middle       : {self.m}")
        print(f"Lower        : {self.l}")
        print(f"Rac          : {self.rac}")
        print(f"Waiting List : {self.wait}")

    
    def book(self,name,age,birth,id,db):
        db[id] = {"id":id,"name": name,"age":age,"birth":birth,}
        print(db[id])
        ...
    def reg(self,db):
        id = 0
        pas.print_tick()
        self.name = input(f"Enter name : ")
        self.age = int(input(f"Enter age : "))
        self.birth = input(f"Select Birth u m l\nEnter Birth : ")
        self.id +=1
        pas.conform(self.birth)
        pas.print_tick(self.birth)
        pas.book(self.name,self.age,self.birth,self.id,db)
        
    def booked(self,db):
        print(db)

    def conform(self,birth):
        
        if birth == 0:
            ...


    def remove(self,db):
        rid = int(input())
        del db[rid]


    

if __name__ == "__main__":
    pas = ticket()
    db = {}
    while True:
        print("\nRailway Ticket Reservation System\n")
        print("1. Book Ticket")
        print("2. Cancel Ticket")
        print("3. Print Booked Tickets")
        print("4. Print Available Tickets")
        print("5. Exit")
        choice = int(input())
        if choice == 1:
            pas.reg(db)
        elif choice == 2:
            pas.remove(db)
        if choice == 3:
            pas.booked(db)
        elif choice == 4:
            pas.print_tick()
    