import sys

try:
    len = 0
    for arg in sys.argv:
        len += 1

    if len == 1: # No argument provided
        exit()

    # In assert statement, if condition is true, nothing happens and if condition is false, AssertionError is raised.
    assert len <= 2  , "more than one argument is provided"

    # another way of throwing assertion error
    try:
        number = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")

    # ternary operator
    print("I'm Even.") if number % 2 == 0 else print("I'm Odd.")
    

except AssertionError as message:
        print(AssertionError.__name__ + ":", message)
