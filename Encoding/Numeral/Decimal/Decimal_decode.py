from Encoding.Numeral.Hex.Hex_decode import hex_to_chr

# list or singular item
# format -> 99 or [99, ...]


# decimal -> hex
# Will leave 0x in front of hexcode!
def int_to_hex(int_list):
    if isinstance(int_list, int):
        return hex(int_list)
    else:
        hex_list = []

        for integer in int_list:
            hex_list.append(hex(integer))

        return hex_list


# decimal -> binary
# Will leave 0b in front of binary!
def int_to_bin(int_list):
    if isinstance(int_list, int):
        return bin(int_list)
    else:
        bin_list = []

        for integer in int_list:
            bin_list.append(bin(integer))

        return bin_list


# decimal -> hex -> plaintext
def int_to_chr(integer):
    hexcode = int_to_hex(integer)[2:]

    return hex_to_chr(hexcode)
