import sys


def print_output(template, value):
    """Prints the output in the given format.

    Args:
        template (str): The template string.
        value (int): The value to be formatted in the template.
    """
    print(template.format(value))


def count_char(text):
    """Counts the number of characters in the given text.

    Args:
        text (str): The input text.
    """
    var = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 \n'
    upper = sum(1 for i in text if i >= 'A' and i <= 'Z')
    lower = sum(1 for i in text if i >= 'a' and i <= 'z')
    digit = sum(1 for i in text if i >= '0' and i <= '9')
    spaces = sum(1 for i in text if i == ' ' or i == '\n')
    others = sum(1 for i in text if i not in var)

    print_output("The text contains {:} characters:", len(text))
    print_output("{:} upper letters", upper)
    print_output("{:} lower letters", lower)
    print_output("{:} punctuation marks", others)
    print_output("{:} spaces", spaces)
    print_output("{:} digits", digit)


def main():
    """Main function"""
    text = ""
    try:
        assert (len(sys.argv) < 3), "more than one argument is provided"

        if len(sys.argv) == 1:
            print("What is the text to count?")
            while True:
                char = sys.stdin.read(1)
                text += char
                if char == '\n' or not char:
                    break
        elif len(sys.argv) == 2:
            text = sys.argv[1]

        count_char(text)

    except Exception as e:
        print(type(e).__name__+":", e)
        exit(1)
    except KeyboardInterrupt:
        print("\nExiting...")
        exit(0)


if __name__ == "__main__":
    """Executes the main function when the script is run directly."""
    # This block is commonly used to contain code that should only be executed
    # when the script is run directly, not when it is imported as a module.
    main()
