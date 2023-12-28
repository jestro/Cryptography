from Encoding.HelperFunctionsEnc.Binary import is_bin
from Encoding.HelperFunctionsEnc.Hex import is_hex
from HelperFunctionsGlobal.int_manip import is_int
from HelperFunctionsGlobal.list_manip import is_list
from HelperFunctionsGlobal.string_manip import is_string


def is_codetype(data):
    if is_list(data):
        data = data[0]
    if is_string(data):
        if is_hex(data):
            return "hex"
        elif is_bin(data):
            return "binary"
        else:
            return "str"
    elif is_int(data):
        return "int"
