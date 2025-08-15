import sys


def words_greater_than_n():
    try:
        assert len(sys.argv) == 3 and sys.argv[2].isdigit() and not sys.argv[1].isdigit(), (
            "AssertionError: the arguments are bad"
            )

        if int(sys.argv[2]):
            n = int(sys.argv[2])
        string = sys.argv[1]
        check_lambda = lambda word: len(word) > n  # noqa: E731
        new_list = [word for word in string.split() if check_lambda(word)]
        print(new_list)
    except Exception as error:
        print(error)


def main():
    try:
        words_greater_than_n()
    except Exception as e:
        print(f"Error message: {e}")


if __name__ == "__main__":
    main()
