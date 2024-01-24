""" Reproduce the behavior of the function filter """


def ft_filter(func, list) -> list:
    """ft_filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    # format for list comprehensions :
    # [expression for item in iterable if condition == True]
    if func is None:
        return (i for i in list if i)
    else:
        return (i for i in list if func(i))

# -------------------------------------------------
# TESTER
# -------------------------------------------------
# def print_list(list, message):
#     """ Print a list
#     Args: list: list to be printed
#           message: message to be printed before the list
#     Returns: None"""
#     print(message)
#     for c in list:
#         print(c)


# def main():
#     """Main function"""
#     letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o', 0, 1, True, False]
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     filtered_None = ft_filter(None, letters)
#     print_list(filtered_None, "Filtered List when function is None:")
#     filtered = ft_filter(lambda x: x in vowels, letters)
#     print_list(filtered, "Filtered List when function is valid:")


# if __name__ == "__main__":
#     main()
