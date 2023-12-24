# list or singular item
# format -> '0x63' or ['0x63', ...]

# hex -> decimal
def hex_to_int(hex_list):
    if isinstance(hex_list, str):
        return int(hex_list, 16)

    int_list = []

    for hex_char in hex_list:
        int_list.append(int(hex_char, 16))

    return int_list


# Only possible if the hex items' decimal values are ASCII
# hex -> decimal -> plaintext
def hex_to_chr(hex_list):
    if isinstance(hex_list, str):
        return chr(int(hex_list, 16))

    plaintext = ""

    for hex_char in hex_list:
        plaintext += chr(int(hex_char, 16))

    return plaintext


# hex -> decimal -> binary
def hex_to_bin(hex_list):
    if isinstance(hex_list, str):
        return bin(int(hex_list, 16))

    bin_list = []

    for hex_char in hex_list:
        bin_list.append(bin(int(hex_char, 16)))

    return bin_list
