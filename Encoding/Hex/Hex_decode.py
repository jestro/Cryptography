# list or singular item
# format -> '0x63' or ['0x63', ...]

# hex -> decimal
def hex_decode_decimal(hex_list):
    if isinstance(hex_list, str):
        return int(hex_list, 16)

    ascii_list = []

    for hex_char in hex_list:
        ascii_list.append(int(hex_char, 16))

    return ascii_list


# Only possible if the hex items' decimal values are ASCII
# hex -> decimal -> plaintext
def hex_decode_plaintext(hex_list):
    if isinstance(hex_list, str):
        return chr(int(hex_list, 16))

    plain_text = ""

    for hex_char in hex_list:
        plain_text += chr(int(hex_char, 16))

    return plain_text


# hex -> decimal -> binary
def hex_decode_binary(hex_list):
    if isinstance(hex_list, str):
        return bin(int(hex_list, 16))

    binary_list = []

    for hex_char in hex_list:
        binary_list.append(bin(int(hex_char, 16)))

    return binary_list
