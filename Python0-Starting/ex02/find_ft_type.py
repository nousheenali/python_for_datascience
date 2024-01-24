"""
Write a function that prints the object types and returns 42.
"""
def all_thing_is_obj(object: any) -> int: 
    # use class attribute to get the type of an object. Alternatively, we can use type() function
    if object.__class__ in {list, tuple, set, dict}:
        print(object.__class__.__name__.capitalize() + " :",object.__class__)
    if (object.__class__ == str):
        print( object + " is in the kitchen :",object.__class__)
    if (object.__class__ == int):
        print("Type not found")
    return 42
