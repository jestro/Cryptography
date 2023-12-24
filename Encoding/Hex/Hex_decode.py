from Encoding.ASCII.ASCII_encode import ascii_encode


# "637279" -> b'cry' (bytes)
def hex_decode_plaintext(hexstring):
    return bytes.fromhex(hexstring)


# "637279" -> 6517369
def hex_decode_number(hexstring):
    hex_values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    hex_eq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    hexstring = hexstring.upper()

    number = 0

    for index in range(0, len(hexstring)):
        last_index = len(hexstring) - 1
        number += hex_eq[hex_values.index(hexstring[index])] * pow(16, last_index - index)
    return number
