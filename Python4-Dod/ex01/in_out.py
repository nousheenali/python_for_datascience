def square(x: int | float) -> int | float:
    """
    This function takes a number and returns the
    square of that number"""
    return x * x


def pow(x: int | float) -> int | float:
    """
    This function takes a number and returns the power
    of that number to itself."""
    return x ** x


# def outer(x: int | float, function) -> object:
#     count = 0
#     def inner() -> float:
#         nonlocal count
#         count += 1
#         out = x
#         for i in range(count):
#             out = function(out)
#         return out
#     return inner


def outer(x: int | float, function) -> object:
    """
    This function takes a number and a function and returns a function
    that will apply the given function to the given number.
    """
    count = x

    def inner() -> float:
        nonlocal count
        count = function(count)
        return count
    return inner


"""
NOTE1:
The nonlocal keyword is used to work with variables inside nested
functions, where the variable should not belong to the inner function
but to the parent function.
IT works in exactly the same way as the global statement, except
that it is used to refer to variables that are neither global nor
local to the function.
"""
