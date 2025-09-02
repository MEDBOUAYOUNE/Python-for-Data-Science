class calculator:
    """Calculator class to perform vector operations."""
    def __init__(self, V1: list[float], V2: list[float] = None):
        """ Constructor to initialize the calculator with two vectors."""
        self.V1 = V1
        self.V2 = V2

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """ compute product of two vectors"""
        if len(V1) != len(V2):
            raise ValueError("Vectors must be of the same length")
        result = sum(x * y for x, y in zip(V1, V2))
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add two vectors element-wise."""
        if len(V1) != len(V2):
            raise ValueError("Vectors must be of the same length")
        result = [float(x + y) for x, y in zip(V1, V2)]
        print(f"Add Vector is: {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtract two vectors element-wise."""
        if len(V1) != len(V2):
            raise ValueError("Vectors must be of the same length")
        result = [float(x - y) for x, y in zip(V1, V2)]
        print(f"Sub Vector is: {result}")