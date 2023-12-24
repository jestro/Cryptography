def ascii_decode(ascii_list):
    plain_text = ""

    for ascii_char in ascii_list:
        plain_text += chr(ascii_char)

    return plain_text
