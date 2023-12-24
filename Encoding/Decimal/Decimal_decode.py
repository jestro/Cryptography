# list or singular item
# format -> 99 or [99, ...]

# decimal -> hex
def int_to_hex(int_list):
    if isinstance(int_list, int):
        return hex(int_list)
    else:
        hex_list = []

        for integer in int_list:
            hex_list.append(hex(integer))

        return hex_list


# Only possible if decimals are ASCII
# decimal -> plaintext
def int_to_chr(int_list):
    if isinstance(int_list, int):
        return chr(int_list)
    else:
        plaintext = ""

        for integer in int_list:
            plaintext += chr(integer)

        return plaintext


# decimal -> binary
def int_to_bin(int_list):
    if isinstance(int_list, int):
        return bin(int_list)
    else:
        bin_list = []

        for integer in int_list:
            bin_list.append(bin(integer))

        return bin_list
