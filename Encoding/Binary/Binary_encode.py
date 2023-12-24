# cry -> ['0b1100011', '0b1110010', '0b1111001']
def binary_encode_plaintext(plaintext):
    binary_list = []

    for plaintext_char in plaintext:
        binary_list.append(bin(ord(plaintext_char)))

    return binary_list


# [0x63, 0x72, 0x79] -> ['0b1100011', '0b1110010', '0b1111001']
def binary_encode_hex(hex_list):
    binary_list = []

    for hex_char in hex_list:
        binary_list.append(bin(hex_char))

    return binary_list