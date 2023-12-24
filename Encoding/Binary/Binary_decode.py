# ['0b1100011', '0b1110010', '0b1111001'] -> 'cry'
def binary_decode_plaintext(binary_list):
    plain_text = ""

    for binary_char in binary_list:
        plain_text += chr(int(binary_char, 2))

    return plain_text