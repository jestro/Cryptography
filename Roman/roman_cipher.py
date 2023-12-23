PLAIN_ALPHABET = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                  "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def get_cipher_alphabets():
    cipher_alphabets = []

    for shift in range(len(PLAIN_ALPHABET)):
        if shift == 0:
            continue

        cipher_alphabet = []

        for char_index in range(len(PLAIN_ALPHABET)):
            if shift + char_index >= len(PLAIN_ALPHABET):
                cipher_alphabet.append(PLAIN_ALPHABET[(char_index + shift) - 26])
            else:
                cipher_alphabet.append(PLAIN_ALPHABET[char_index + shift])

        cipher_alphabets.append(cipher_alphabet)

    return cipher_alphabets


def get_cipher_alphabet(shift):
    cipher_alphabet = []

    for char_index in range(len(PLAIN_ALPHABET)):
        if shift + char_index >= len(PLAIN_ALPHABET):
            cipher_alphabet.append(PLAIN_ALPHABET[(char_index + shift) - 26])
        else:
            cipher_alphabet.append(PLAIN_ALPHABET[char_index + shift])

    return cipher_alphabet


def roman_decode(cipher):
    cipher = cipher.upper()

    print("\nCipher: ")

    for cipher_alphabet in get_cipher_alphabets():
        plaintext = ""

        for char in cipher:
            if char == " ":
                plaintext += " "
            else:
                plaintext += PLAIN_ALPHABET[cipher_alphabet.index(char)]

        print(plaintext)


def roman_encode(plaintext, shift):
    cipher_alphabet = get_cipher_alphabet(shift)

    plaintext = plaintext.upper()
    cipher = ""

    print("\nEncode: ")

    if shift == 0:
        print(plaintext)
    else:
        for char in plaintext:
            if char == " ":
                cipher += " "
            else:
                cipher += cipher_alphabet[PLAIN_ALPHABET.index(char)]
        print(cipher)
