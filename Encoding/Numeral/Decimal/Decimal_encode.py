from Encoding.HelperFunctionsEnc.Hex import merge_hex_array
from Encoding.Numeral.Hex.Hex_decode import hex_to_int
from Encoding.Numeral.Hex.Hex_encode import chr_to_hex

# list or singular item
# format -> c or cry


# plaintext -> hex -> decimal
def chr_to_int(plaintext):
    return hex_to_int(merge_hex_array(chr_to_hex(plaintext)))
