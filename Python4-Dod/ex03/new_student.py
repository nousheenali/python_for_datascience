import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generates a random 15-character string composed of lowercase
    letters. It is intended to be used as the default value for the
    id field in the Student class."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    Represents a student. The name and surname fields are required.
    The active field is optional and defaults to True. The login
    field is read-only and is automatically generated from the name
    and surname fields. The id field is read-only and is
    automatically generated using the generate_id function.
    """
    name: str
    surname: str
    active: bool = True
    login: str = field(default="", init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        self.login = self.name[0] + self.surname[0:3]


"""
REFERENCES:
https://docs.python.org/3/library/dataclasses.htmlhttps://www.dataquest.io/blog/how-to-use-python-data-classes/
https://www.packetcoders.io/python-data-classes/
NOTES:
- The @dataclass decorator is used to automatically generate
special methods (init, repr, eq etc.) for the Student class.
- The default_factory parameter is used to specify a function that
will be called to generate the default value for the id field.
- The field function is used to specify the default_factory parameter.
- with __post_init__ run after auto-generated __init__ thereby adding
functionality to the data class
- init=False argument in the field function is used to exclude a
field from the automatically generated __init__ method when dataclass
creates the class.
"""
