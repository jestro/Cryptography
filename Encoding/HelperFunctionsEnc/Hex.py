# ['0x63', '0x72', '0x79'] -> "637279"
def merge_hex_array(hexarray):
    hexstring = ""

    for hexcode in hexarray:
        hexstring += remove_0x(hexcode)

    return hexstring


# "0x63" -> "63"
def remove_0x(hexadecimal):
    if hexadecimal[:2] == "0x":
        hexadecimal = hexadecimal[2:]

    return hexadecimal


# "0xA" -> True
# "A" -> False
def is_hex(hexadecimal):
    return hexadecimal[:2] == "0x"
