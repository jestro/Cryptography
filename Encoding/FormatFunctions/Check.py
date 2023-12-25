def is_codetype(data):
    if isinstance(data, list):
        data = data[0]
    if isinstance(data, str):
        if data[:2] == "0x":
            return "hex"
        elif data[:2] == "0b":
            return "binary"
        else:
            return "str"
    elif isinstance(data, int):
        return "int"
