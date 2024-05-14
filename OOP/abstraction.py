from abc import ABC, abstractmethod
class area:

    def __init__(self,l=None,b=None,a=None ) -> None:
        self.l = l
        self.b = b
        self.a = a
    @abstractmethod
    def rectangle(self):
        return self.l*self.b
    
    @abstractmethod
    def square(self):
        return self.b**2
    
class Subclass(area):
    def __init__(self, l=None, b=None, a=None) -> None:
        super().__init__(l, b, a)

    def rectangle(self):
        return super().rectangle()
    def square(self):
        return super().square()
    

a1=Subclass(l=5,b=3,a=4)
print(a1.rectangle())
