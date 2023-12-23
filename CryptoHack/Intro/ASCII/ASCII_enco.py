def ascii_decode(plaintext):
    cipher = ""

    for plaintext_char in plaintext:
        cipher += ord(plaintext_char)

    return cipher
