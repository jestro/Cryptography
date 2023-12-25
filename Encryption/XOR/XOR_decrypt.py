from Encoding.Binary.Binary_decode import bin_to_chr
from Encoding.FormatFunctions.Binary import remove_0b
from Encryption.XOR.Helper import key_init
from Encryption.XOR.XOR_encrypt import xor_encrypt


def xor_decrypt(data, key):
    key_list = key_init(key)
    xor = []

    for binary in range(len(data)):
        key = remove_0b(key_list[binary % len(key_list)])
        binary = remove_0b(data[binary])
        xor_binary = ""
        for number in range(len(binary)):
            if binary[number] == key[number]:
                xor_binary += "0"
            else:
                xor_binary += "1"

        xor.append(xor_binary)

    return bin_to_chr(xor)


print(xor_encrypt("c", "k"))
