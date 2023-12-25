from Encoding.Binary.Binary_encode import chr_to_bin
from Encoding.FormatFunctions.Binary import remove_0b
from Encryption.XOR.Helper import key_init


def xor_encrypt(plaintext, key):
    bin_list = bin_init(plaintext)
    key_list = key_init(key)

    xor = []

    for binary in range(len(bin_list)):
        key = remove_0b(key_list[binary % len(key_list)])
        binary = remove_0b(bin_list[binary])
        xor_binary = ""
        for number in range(len(binary)):
            if binary[number] == key[number]:  # if the number in the binary is the same as the number in the key
                xor_binary += "0"
            else:
                xor_binary += "1"

        xor.append(xor_binary)

    return xor


def bin_init(plaintext):
    if len(plaintext) == 1:
        return [chr_to_bin(plaintext)]
    else:
        return chr_to_bin(plaintext)