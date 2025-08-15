import sys


def building() -> None:
    """
        This function analyzes a given text and prints the number of:
            - Uppercase letters
            - Lowercase letters
            - Punctuation marks
            - Spaces
            - Digits

        Arguments:
        - If no argument is passed, the function will prompt the /
         user to enter the text via standard input.
        - If one argument is provided, it will be used as the text to analyze.
        - If more than one argument is provided, the script /
         raises an AssertionError.

        Example:
        $ python script.py "Hello, World! 123"
        The text contains 17 characters:
        2 upper letters
        8 lower letters
        2 punctuation marks
        2 spaces
        3 digits
    """
    assert len(sys.argv) <= 2, (
        "AssertionError: more than one argument is provided")
    if len(sys.argv) == 1:
        print("What is the text to count?")
        text = sys.stdin.readline()
    else:
        text = sys.argv[1]
    print(f"The text contains {len(text)} characters:")
    print(f"{len(list(filter(lambda x: x.isupper(), text)))} upper letters")
    print(f"{len(list(filter(lambda x: x.islower(), text)))} lower letters")
    print(f"{len(list(filter(lambda x: not x.isalnum() and not x.isspace(), text)))} punctuation marks")
    print(f"{len(list(filter(lambda x: x.isspace(), text)))} spaces")
    print(f"{len(list(filter(lambda x: x.isdigit(), text)))} digitss")


def main() -> None:
    try:
        building()
    except Exception as e:
        print(f"Error message: {e}")


if __name__ == "__main__":
    main()
