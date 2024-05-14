class students:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.laptop = self.Laptop()

    def show(self):
        print(f"Name : {self.name}\nRoll no : {self.rollno}")

    # Inner Class
    class Laptop:

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 16
        
s1 = students('Ansal', '2020PECCB101')
s1.show()
print(f"Laptop brand : {s1.laptop.brand}")
