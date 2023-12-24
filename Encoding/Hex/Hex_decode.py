# ['0x63', '0x72', '0x79'] -> [99, 114, 121]
# '0x63' -> 99
def hex_decode_number(hex_list):
    if isinstance(hex_list, str):
        return int(hex_list, 16)

    ascii_list = []

    for hex_char in hex_list:
        ascii_list.append(int(hex_char, 16))

    return ascii_list


# ['0x63', '0x72', '0x79'] -> [99, 114, 121] -> 'cry'
# '0x63' -> 99 -> 'c'
def hex_decode_plaintext(hex_list):
    if isinstance(hex_list, str):
        return chr(int(hex_list, 16))

    plain_text = ""

    for hex_char in hex_list:
        plain_text += chr(int(hex_char, 16))

    return plain_text


# ['0x63', '0x72', '0x79'] -> [99, 114, 121] -> ['0b1100011', '0b1110010', '0b1111001']
# '0x63' -> 99 -> '0b1100011'
def hex_decode_binary(hex_list):
    if isinstance(hex_list, str):
        return bin(int(hex_list, 16))

    binary_list = []

    for hex_char in hex_list:
        binary_list.append(bin(int(hex_char, 16)))

    return binary_list
