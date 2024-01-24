import sys


def print_morse(text):
    """Prints the morse code of the given text.
    Args: text (str): The text to be converted to morse code."""
    NESTED_MORSE = {" ": "/", "A": ".-", "B": "-...", "C": "-.-.",
                    "D": "-..", "E": ".", "F": "..-.", "G": "--.",
                    "H": "....", "I": "..", "J": ".---", "K": "-.-",
                    "L": ".-..", "M": "--", "N": "-.", "O": "---",
                    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...",
                    "T": "-", "U": "..-", "V": "...-", "W": ".--",
                    "X": "-..-", "Y": "-.--", "Z": "--..",  "0": "-----",
                    "1": ".----", "2": "..---", "3": "...--", "4": "....-",
                    "5": ".....", "6": "-....", "7": "--...", "8": "---..",
                    "9": "----."
                    }
    print(" ".join(NESTED_MORSE[i.upper()] for i in text))


def main():
    """Checks the arguments and calls print_morse function."""
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        # checks all characters in argv[1] are either alphanumeric or space
        assert all(
            c.isalnum() or c.isspace() for c in sys.argv[1]
            ), "the arguments are bad"
        print_morse(sys.argv[1])
    except AssertionError as message:
        print(AssertionError.__name__ + ":", message)
    except Exception as e:
        print(type(e).__name__ + ":", e)


if __name__ == "__main__":
    main()

# print(NESTED_MORSE[i] for i in sys.argv[1].upper()) --> gives an error
# print(" ".join(NESTED_MORSE[i.upper()] for i in sys.argv[1])) --> works
# This is beacuse the first one is a generator inside print. However, the
# print function expects values to be printed, and a generator expression
# itself is not a value but a generator object. Therefore, it raises an error.
# The second one is a generator expression(Values are generated one at a time
# and not stored in memory until needed) inside the join function. The
# join function expects an iterable of strings, and the generator expression
# produces strings (NESTED_MORSE[i.upper()]), so it works as expected.
