from collections.abc import Collection

def all_thing_is_obj(object: any) -> int:
    if isinstance(object, Collection):
        if isinstance(object, str):
            print(f"{object}  is in the kitchen : {type(object)}")
        else:
            print(f"{type(object).__name__} : {type(object)}")
    else:
        print("Type not found")
    return 42
