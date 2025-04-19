import sys

print(len(sys.argv))
try:
    assert len(sys.argv) == 2, "AssertionError: argument is not an integer"
    assert sys.argv[1].isdigit(), "AssertionError: argument is not an integer"

    value = int(sys.argv[1])

    if value % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

except AssertionError as error:
    print(error)
