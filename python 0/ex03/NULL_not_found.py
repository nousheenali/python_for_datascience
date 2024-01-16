def NULL_not_found(object: any) -> int: 

    types_dict = {
        "NoneType": "Nothing",
        "float": "Cheese",
        "int": "Zero",
        "str": "Empty",
        "bool": "Fake",
    }

    # NaN is a special value used to represent the result of undefined or unrepresentable operations.
    #  NaN is considered unordered, and the IEEE standard defines that NaN is not equal to itself.
    if (object is None or object != object or object == 0 or object == '' or object == False): 
        print(types_dict[object.__class__.__name__] +":", object, object.__class__)

    else:
        print("Type not Found")

    return 1