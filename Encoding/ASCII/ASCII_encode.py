# cry -> [99, 114, 121]
def ascii_encode(plaintext):
    ascii_list = []

    for plaintext_char in plaintext:
        ascii_list.append(ord(plaintext_char))

    return ascii_list
