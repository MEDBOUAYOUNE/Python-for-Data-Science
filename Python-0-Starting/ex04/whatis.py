import sys

def isNumber(arg: str) -> bool:
    if not arg:
        return False
    if arg[0] == "-":
        return arg[1:].isdigit() and len(arg) > 1 
    return arg.isdigit()

try:
    assert len(sys.argv) == 2, "AssertionError: argument is not an integer"
    print(isNumber(sys.argv[1]))
    assert  isNumber(sys.argv[1]), "AssertionError: argument is not an integer"

    value = int(sys.argv[1])

    if value % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

except AssertionError as error:
    print(error)
