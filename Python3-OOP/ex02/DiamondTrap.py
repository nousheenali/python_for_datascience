from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing the King class."""

    def __init__(self, first_name, is_alive=True):
        """Constructor for the King class."""
        super().__init__(first_name, is_alive)

    def set_eyes(self, value):
        """Method to set the eyes attribute."""
        self.eyes = value

    def set_hairs(self, value):
        """Method to set the hairs attribute."""
        self.hairs = value

    def get_eyes(self):
        """Method to get the eyes attribute."""
        return self.eyes

    def get_hairs(self):
        """Method to get the hairs attribute."""
        return self.hairs

    # def printHello(self):
    #     print("Hello from class King")


"""
    print(King.__mro__) to see the Method Resolution order(MRO)
    which is the order in which Python looks for a method in a
    hierarchy of classes in case of diamond inheritance
    # https://www.youtube.com/watch?v=PSMYqfMP3Cs


    Joffrey.printHello() will follow C linearization and will
    check the MRO of the class King and check for printHello()
    in King Class and then in Baratheon and then in Lannister
    and then in Character class and then in Object class.
"""
