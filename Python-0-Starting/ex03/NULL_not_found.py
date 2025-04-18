def NULL_not_found(object: any) -> int:
    object_name = {
        "NoneType" : "Nothing",
        "float" : "Cheese",
        "int" : "Zero",
        "str" : "Empty",
        "bool" : 'Fake',

    }

    object_type = type(object)

    # i guess this check is a hardcode, but it think should check by value not type it is easy too.
    if object and object_type is str:
        print("Type not Found")
        return 1

    print(f"{object_name[object_type.__name__]} : {object} : {object_type}")
    return 0

