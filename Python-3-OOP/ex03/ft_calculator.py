class calculator:
    """"Calculator class to perform basic arithmetic operations on a list of numbers."""
    def __init__(self, numbers: list):
        """Constructor to initialize the calculator with a list of numbers."""
        self.numbers = numbers

    def __add__(self, object) -> None:
        """Add a number to each element in the list."""
        self.numbers = [x + object for x in self.numbers]
        print(self.numbers)

    def __mul__(self, object) -> None:
        """Multiply each element in the list by a number."""
        self.numbers = [x * object for x in self.numbers]
        print(self.numbers)

    def __sub__(self, object) -> None:
        """Subtract a number from each element in the list."""
        self.numbers = [x - object for x in self.numbers]
        print(self.numbers)

    def __truediv__(self, object) -> None:
        """Divide each element in the list by a number."""
        if object == 0:
            raise ValueError("Cannot divide by zero")
        self.numbers = [x / object for x in self.numbers]
        print(self.numbers)