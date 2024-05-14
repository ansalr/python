class Car:
    def __init__(self,name,year,price) -> None:
        self.name = name
        self.year = year
        self.price = price

    def price_increse(self):
        return int(self.price*1.15)

class SuperCar(Car):

    def __init__(self, name, year, price,cc) -> None:
        super().__init__(name, year, price)
        self.cc = cc


honda = SuperCar("city",2015,1000000,1500)
tata = SuperCar

("Bolt",1016,600000,1000)

honda.cc = 1500
print(honda.__dict__)
print(tata.__dict__)
print(honda.price_increse())
