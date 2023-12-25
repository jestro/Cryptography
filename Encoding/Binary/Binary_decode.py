from HelperFunctions.string_manip import split

# list or singular item
# format -> '0b1100011' or ['0b1100011', ...]


# binary -> decimal
def bin_to_int(bin_list):
    if isinstance(bin_list, str):
        return int(bin_list, 2)

    int_list = []

    for binary in bin_list:
        int_list.append(int(binary, 2))

    return int_list


# Only possible if the binary items are Decimal
# binary -> decimal -> plaintext
def bin_to_chr(bin_list):
    # All ASCII characters are 7 bits long (for binary strings)
    if isinstance(bin_list, str):
        bin_list = split(bin_list, 7)

    plaintext = ""

    for binary in bin_list:
        plaintext += chr(int(binary, 2))

    return plaintext


# binary -> decimal -> hex
def bin_to_hex(bin_list):
    if isinstance(bin_list, str):
        return hex(int(bin_list, 2))

    hex_list = []

    for binary in bin_list:
        hex_list.append(hex(int(binary, 2)))

    return hex_list
