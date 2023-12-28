from Encoding.FormatFunctions.Binary import remove_0b
from Encoding.FormatFunctions.Hex import remove_0x
from HelperFunctions.string_manip import split


# plaintext -> ASCII (if singular) / ASCII list
def chr_to_ascii_list(plaintext):
    if len(plaintext) == 1:
        return ord(plaintext)

    ascii_list = []

    for char in plaintext:
        ascii_list.append(ord(char))

    return ascii_list


# binary list / binary string -> ASCII (if singular) / ASCII list
def bin_to_ascii_list(bin_list):
    if isinstance(bin_list, str):
        bin_list = remove_0b(bin_list)
        bin_list = split(bin_list, 7)

    if len(bin_list) == 1:
        return int(bin_list[0], 2)

    ascii_list = []

    for bin_char in bin_list:
        ascii_list.append(int(bin_char, 2))

    return ascii_list


# hex list / hex string -> ASCII (if singular) / ASCII list
def hex_to_ascii_list(hex_list):
    if isinstance(hex_list, str):
        hex_list = remove_0x(hex_list)
        hex_list = split(hex_list, 2)

    if len(hex_list) == 1:
        return int(hex_list[0], 16)

    ascii_list = []

    for hex_char in hex_list:
        ascii_list.append(int(hex_char, 16))

    return ascii_list
