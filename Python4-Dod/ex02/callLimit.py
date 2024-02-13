def callLimit(limit: int):
    """
    Decorator to limit the number of times a function can be called
    """
    count = 0

    def callLimiter(function):
        """
        Inner function that will be returned as the actual decorator
        """

        def limit_function(*args: any, **kwds: any):
            """
            Innermost function that will be called when the decorated
            function is called. It will check if the function has been
            called more than the limit times and if not, it will call
            the decorated function. If the limit is reached, it will
            print an error message."""
            nonlocal count
            if count < limit:
                count += 1
                val = function(*args, **kwds)
                return val
            else:
                print(f"Error: {function} call too many times")
        return limit_function
    return callLimiter


"""
References:
https://builtin.com/data-science/python-wrapper

@callLimit(3)
def f():
    print ("f()")

for i in range(3):
    f()

- When @callLimit(3) decorates the function f, This leads to the
execution of the outer function callLimit with limit set to 3. The
outer function returns the inner function callLimiter, which is then
applied to the function f. The inner function callLimiter returns the
innermost function limit_function as the actual decorator. When f()
is called, it is now equivalent to calling the limit_function returned
by the decorator.
"""
