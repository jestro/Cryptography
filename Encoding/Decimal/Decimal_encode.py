from Encoding.FormatFunctions.Hex import merge_hex_array
from Encoding.Hex.Hex_decode import hex_to_int
from Encoding.Hex.Hex_encode import chr_to_hex

# list or singular item
# format -> c or cry


# plaintext -> ASCII list
def chr_to_ascii_array(plaintext):
    if len(plaintext) == 1:
        return ord(plaintext)

    ascii_list = []

    for char in plaintext:
        ascii_list.append(ord(char))

    return ascii_list


# plaintext -> hex -> decimal
def chr_to_int(plaintext):
    return hex_to_int(merge_hex_array(chr_to_hex(plaintext)))
