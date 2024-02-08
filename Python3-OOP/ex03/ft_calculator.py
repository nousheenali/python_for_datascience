class calculator:
    """
    This class is a simple calculator that can perform
    addition, subtraction, multiplication, and division
    of a vector of numbers with scalar.
    """
    def __init__(self, vector) -> None:
        """ The constructor of Calculator class"""
        self.vector = vector

    def __add__(self, object) -> None:
        """ Method adds a scalar to the vector"""
        new_vector = [x + object for x in self.vector]
        self.vector = new_vector
        print(self.vector)

    def __mul__(self, object) -> None:
        """ Method to multiply a scalar to the vector"""
        new_vector = [x * object for x in self.vector]
        self.vector = new_vector
        print(self.vector)

    def __sub__(self, object) -> None:
        """ Method to subtract a scalar from the vector"""
        new_vector = [x - object for x in self.vector]
        self.vector = new_vector
        print(self.vector)

    def __truediv__(self, object) -> None:
        """ Method to divide the vector by a scalar"""
        try:
            if (object == 0):
                raise ValueError("Division by zero is not allowed")
            new_vector = [x / object for x in self.vector]
            self.vector = new_vector
            print(self.vector)
        except ValueError as e:
            print(type(e).__name__+":", e)


"""
NOTE1:
    *args and **kwargs in Python
    https://www.geeksforgeeks.org/args-kwargs-python/
"""
