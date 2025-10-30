class Person:
    """Base class representing a person with basic attributes."""
    
    def __init__(self, name: str, id_num: int):
        """Initialize a person with name and ID number.
        
        Args:
            name (str): Person's name
            id_num (int): Identification number
        """
        self.name = name
        self.id_num = id_num
        print("Person created")
    
    def details(self) -> None:
        """Display person's details."""
        print(f"Name: {self.name}")
        print(f"ID Number: {self.id_num}")


class Employee(Person):
    """Employee class inheriting from Person with additional attributes."""
    
    def __init__(self, name: str, id_num: int, salary: float, post: str):
        """Initialize an employee.
        
        Args:
            name (str): Employee's name
            id_num (int): Employee's ID number
            salary (float): Employee's salary
            post (str): Employee's position
        """
        super().__init__(name, id_num)
        self.salary = salary
        self.post = post
    
    def details(self) -> None:
        """Display employee's complete details."""
        super().details()
        print(f"Salary: {self.salary}")
        print(f"Post: {self.post}")


class Dog:
    """Base class representing a dog with basic abilities."""
    
    def __init__(self, name: str):
        """Initialize a dog.
        
        Args:
            name (str): Dog's name
        """
        self.name = name
        self.moves = []  # Instance variable instead of class variable
    
    def moves_setup(self) -> None:
        """Set up basic movement abilities."""
        self.moves.extend(['walk', 'run'])
    
    def get_moves(self) -> list:
        """Return list of available moves.
        
        Returns:
            list: Available moves
        """
        return self.moves


class Superdog(Dog):
    """Enhanced dog with additional abilities."""
    
    def moves_setup(self) -> None:
        """Set up enhanced movement abilities including flying."""
        super().moves_setup()
        self.moves.append('fly')


def main():
    # Test Employee class
    employee = Employee("Ansal", 14423, 200000, "Intern")
    print("Employee Details:")
    employee.details()
    print("\n")
    
    # Test Superdog class
    dog = Superdog('Freddy')
    print(f"Dog's name: {dog.name}")
    dog.moves_setup()
    print(f"Available moves: {dog.get_moves()}")


if __name__ == "__main__":
    main()
