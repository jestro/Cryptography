from Encoding.Numeral.Binary.Binary_decode import bin_to_chr, bin_to_hex
from Encryption.XOR.XOR import xor


def xor_cipher(data, key, code_type="str"):
    if code_type == "str":
        return bin_to_chr(xor(data, key))

    elif code_type == "binary":
        return xor(data, key)

    elif code_type == "hex":
        return bin_to_hex(xor(data, key))

    else:
        print("Invalid code type.")
