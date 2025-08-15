def NULL_not_found(object: any) -> int:
    """
        Identifies and categorizes a 'null-like' value based on its type and falsy value.

        The function checks the provided object and prints a specific label depending on its type 
        and whether it's considered "falsy" (i.e., evaluates to False in a boolean context).

    """

    if object is None:
        print(f'Nothing: {object} {type(object)}')
        return 0
    elif type(object) is float and object != object:
        print(f'Cheese: {object} {type(object)}')
        return 0
    elif type(object) is int and not object:
        print(f'Zero: {object} {type(object)}')
        return 0
    elif type(object) is str and not object:
        print(f'Empty: {object} {type(object)}')
        return 0
    elif type(object) is bool and not object:
        print(f'Fake: {object} {type(object)}')
        return 0
    else:
        print('Type not Found')
        return 1



# $>python tester.py | cat -e
# Nothing: None <class 'NoneType'>$
# Cheese: nan <class 'float'>$
# Zero: 0 <class 'int'>$
# Empty: <class 'str'>$
# Fake: False <class 'bool'>$
# Type not Found$
# 1$
# $>