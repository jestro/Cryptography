# ['0b1100011', '0b1110010', '0b1111001'] -> '1100011110011111001'
def merge_bin_array(binarray):
    binstring = ""

    for binary in binarray:
        binstring += remove_0b(binary)

    return binstring


# '0b1100011' -> '1100011'
def remove_0b(binary):
    if binary[:2] == "0b":
        binary = binary[2:]

    return binary
