
""" Reproduce the behavior of the function filter """

def fun(variable):
    """ Function to filter vowels """
    vowels = ['a', 'e', 'i', 'o', 'u']
    if variable in vowels:
        return True
    else:
        return False
    
def ft_filter(fun, letters):
    """ft_filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    # newlist = [expression for item in iterable if condition == True]
    new_list = (i for i in letters if fun(i))
    return new_list


def main():
    """Main function"""
    letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
    filtered = ft_filter(fun, letters)
    for l in filtered:
        print(l)


if __name__=="__main__":
    main()