import sys
from ft_filter import ft_filter


def main():
    """ Program to filter words in a string of a minimum length
    args: sys.argv[1] -> string to be filtered
          sys.argv[2] -> minimum length of the words to be filtered"""
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        N = int(sys.argv[2])
        new_list = list(
            ft_filter(lambda x: len(x) > N, sys.argv[1].split(' ')))
        print(new_list)
    except AssertionError as message:
        print(AssertionError.__name__ + ":", message)
    except Exception as e:
        print(type(e).__name__ + ":", e)


if __name__ == "__main__":
    main()
