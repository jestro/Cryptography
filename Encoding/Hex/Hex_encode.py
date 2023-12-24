# [99, 114, 121] -> ['0x63', '0x72', '0x79']
# 99 -> '0x63'
def hex_encode_number(number_list):
    if isinstance(number_list, int):
        return hex(number_list)

    hex_list = []

    for number in number_list:
        hex_list.append(hex(number))

    return hex_list


# cry -> [99, 114, 121] -> ['0x63', '0x72', '0x79']
# c -> 99 -> '0x63'
def hex_encode_plaintext(plaintext):
    if len(plaintext) == 1:
        return hex(ord(plaintext))

    hex_list = []

    for plaintext_char in plaintext:
        hex_list.append(hex(ord(plaintext_char)))

    return hex_list


# ['0b1100011', '0b1110010', '0b1111001'] -> [99, 114, 121] -> ['0x63', '0x72', '0x79']
# '0b1100011' -> 99 -> '0x63'
def hex_encode_binary(binary_list):
    if isinstance(binary_list, str):
        return hex(int(binary_list, 2))

    hex_list = []

    for binary_char in binary_list:
        hex_list.append(hex(int(binary_char, 2)))

    return hex_list
