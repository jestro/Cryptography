# [99, 114, 121] -> cry
def ascii_decode_plaintext(ascii_list):
    plain_text = ""

    for ascii_char in ascii_list:
        plain_text += chr(ascii_char)

    return plain_text


# [99, 114, 121] -> ['0x63', '0x72', '0x79']
def ascii_decode_hex(ascii_list):
    hex_list = []

    for ascii_char in ascii_list:
        hex_list.append(hex(ascii_char))

    return hex_list
