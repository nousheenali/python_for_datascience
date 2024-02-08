from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name, is_alive=True):
        """Constructor for the Baratheon class."""
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __str__(self):
        """
        Provides a human-readable representation of the object
        """
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self):
        """
        Provides a representation that can be used to recreate the object
        """
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def die(self):
        """Method die for the Baratheon class."""
        self.is_alive = False


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name, is_alive=True):
        """Constructor for the Lannister class."""
        super(Lannister, self).__init__(first_name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def __str__(self):
        """ Provides a human-readable representation of the object"""
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self):
        """ Provides a representation that can be used to recreate the object
        """
        return f"{self}"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Class method to create a Lannister object."""
        return cls(first_name, is_alive)

    def die(self):
        """Method die for the Lannister class."""
        self.is_alive = False


"""
NOTES:

    NOTE1:
    __str__  provides a human-readable representation of the object.
    __repr__ provides a representation that can be used to recreate the object.

    NOTE2:
    If obj.__str__() is not defined, print(obj) will use obj.__repr__() instead
    If obj.__repr__() is not defined, print(obj) will use obj.__str__() instead

    NOTE3:
    Difference between obj.__str__() and obj.__str__:
    obj.__str__(): This syntax is used to explicitly call the __str__ method on
    the object obj. It invokes the method and returns the result.
    obj.__str__: This syntax is a reference to the __str__ method itself, not a
    call to the method. If you print or use this expression without the
    parentheses, you will see that it returns method representation, not the
    result of calling the method.


    NOTE4:
    The difference between a static method and a class method is:
    https://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python
    * Instance Method in a class takeS the instance(SELF) as the 1st argument,
        Instance attributes are attributes that are not shared by objects.
        Every object has its own copy of the instance attribute.
    * class methods take the class as the first argument,
    * static methods don't take any implicit arguments.
"""
