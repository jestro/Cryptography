# list or singular item
# format -> '0b1100011' or ['0b1100011', ...]

# binary -> decimal
def binary_decode_number(binary_list):
    if isinstance(binary_list, str):
        return int(binary_list, 2)

    ascii_list = []

    for binary_char in binary_list:
        ascii_list.append(int(binary_char, 2))

    return ascii_list


# Only possible if the binary items are Decimal
# binary -> decimal -> plaintext
def binary_decode_plaintext(binary_list):
    if isinstance(binary_list, str):
        return chr(int(binary_list, 2))

    plain_text = ""

    for binary_char in binary_list:
        plain_text += chr(int(binary_char, 2))

    return plain_text


# binary -> decimal -> hex
def binary_decode_hex(binary_list):
    if isinstance(binary_list, str):
        return hex(int(binary_list, 2))

    hex_list = []

    for binary_char in binary_list:
        hex_list.append(hex(int(binary_char, 2)))

    return hex_list
