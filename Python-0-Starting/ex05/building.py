import sys

def building() -> None:
    """  """
    try:
        assert len(sys.argv) <= 2, "AssertionError: more than one argument is provided"
        if len(sys.argv) == 1:
            print("What is the text to count?")
            text = sys.stdin.readline()
        else:
            text = sys.argv[1]
        isdigit = islower = isupper = isspace = mark = 0

        for character in text:
            if character.isdigit():
                isdigit += 1

            elif character.isupper():
                isupper += 1

            elif character.islower():
                islower += 1

            elif character.isspace():
                isspace += 1

            else:
                mark += 1

        print(f"The text contains {isupper + islower + isdigit + isspace + mark} characters:")
        print(f"{isupper} upper letters")
        print(f"{islower} lower letters")
        print(f"{mark} punctuation marks")
        print(f"{isspace} spaces")
        print(f"{isdigit} digits")


    
    except AssertionError as error:
        print(error)


def main():
    building()


if __name__ == "__main__":
    main()