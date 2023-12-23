def ascii_decode(cipher):
    plain_text = ""

    for ascii_char in cipher:
        plain_text += chr(ascii_char)

    return plain_text
