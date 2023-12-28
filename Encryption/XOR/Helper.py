from Encoding.Numeral.Binary.Binary_encode import chr_to_bin
from Encoding.Numeral.Decimal.Decimal_decode import int_to_bin
from Encoding.HelperFunctionsEnc.Binary import format_bin
from Encoding.HelperFunctionsEnc.Check import is_codetype
from Encoding.Numeral.Hex.Hex_decode import hex_to_bin
from HelperFunctionsGlobal.list_manip import is_list


def data_to_bin7b(data):
    bin_list = []

    if is_codetype(data) == "str":
        if len(data) > 1:
            bin_list = chr_to_bin(data)
        else:
            bin_list = [chr_to_bin(data)]

    elif is_codetype(data) == "int":
        if is_list(data):
            for binary in int_to_bin(data):
                bin_list.append(format_bin(binary, 7))
        else:
            bin_list = [format_bin(int_to_bin(data), 7)]

    elif is_codetype(data) == "binary":
        if is_list(data):
            for binary in data:
                bin_list.append(format_bin(binary, 7))
        else:
            bin_list = [format_bin(data, 7)]

    elif is_codetype(data) == "hex":
        if is_list(data):
            for binary in hex_to_bin(data):
                bin_list.append(format_bin(binary, 7))
        else:
            bin_list = [format_bin(hex_to_bin(data), 7)]

    return bin_list
