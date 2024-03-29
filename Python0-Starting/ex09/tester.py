from ft_package.count_in_list import count_in_list
from ft_package.string_operations import capitalize, palindrome


def main():
    '''Main function'''
    print(count_in_list(["toto", "tata", "toto"], "toto"))  # output: 2
    print(count_in_list(["toto", "tata", "toto"], "tutu"))  # output: 0
    print(capitalize("hello"))  # output: HELLO
    print(palindrome("malayalam"))  # output: returns True is palindrome


if __name__ == "__main__":
    main()
