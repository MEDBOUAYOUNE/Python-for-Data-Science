from collections.abc import Collection

def all_thing_is_obj(object: any) -> int:
    if isinstance(object, Collection):
        type_obj = type(object)
        if isinstance(object, str):
            print(f"{object}  is in the kitchen : {type_obj}")
        else:
            print(f"{type_obj.__name__} : {type_obj}")
    else:
        print("Type not found")
    return 42
