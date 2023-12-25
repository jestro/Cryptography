from Encoding.Binary.Binary_encode import chr_to_bin
from Encoding.Decimal.Decimal_decode import int_to_bin
from Encoding.FormatFunctions.Binary import format_bin_8bit
from Encoding.FormatFunctions.Check import is_codetype
from HelperFunctions.list_manip import is_list


def key_init(key):
    key_list = []

    if is_codetype(key) == "str":
        if len(key) > 1:
            key_list = chr_to_bin(key)
        else:
            key_list = [chr_to_bin(key)]

    elif isinstance(key, int):
        if is_list(key):
            for binary in int_to_bin(key):
                key_list.append(format_bin_8bit(binary))
        else:
            key_list = [format_bin_8bit(int_to_bin(key))]

    return key_list
