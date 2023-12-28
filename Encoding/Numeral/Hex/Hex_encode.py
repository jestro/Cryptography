# list or singular item
# format -> c or cry

# plaintext -> ASCII -> hex
def chr_to_hex(plaintext):
    if len(plaintext) == 1:
        return hex(ord(plaintext))

    hex_list = []

    for plaintext_char in plaintext:
        hex_list.append(hex(ord(plaintext_char)))

    return hex_list
