"""
* We cannot create abstract classes directly in Python.
Python provides a module called abc that provides the
infrastructure for defining the base of Abstract Base Classes(ABC).

*class Character derived from the ABC class from the abc module
that makes it an abstract class. A decorator @abstractmethod
is defined to indicate that the function role is an abstract method.
"""
from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract Class"""
    def __init__(self, first_name, is_alive=True):
        """Constructor for the abstract class Character."""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Abstract Method die for the Character class."""
        pass

    def printHello(self):
        print("Hello from class Character")


class Stark(Character):
    """Class Stark derived from Character class"""
    # No need for separate __init__ method unless additional attributes needed
    def die(self):
        """Method die for the Stark class."""
        self.is_alive = False


"""
Abstract Class:
When there is a requirement where a base class should provide default
implementation of certain methods whereas other methods should be open
to being overridden by child classes use abstract classes.
Let's say you want to deploy an application on an Ipad, Android, Iphone
and Desktop application. You work on an important part that will do 95%
of the job in an abstract class. Then you create 4 other small classes
that will implement the abstract method differently for each device.

References:
https://www.geeksforgeeks.org/python-oops-concepts/
https://www.w3schools.com/python/python_classes.asp
"""
