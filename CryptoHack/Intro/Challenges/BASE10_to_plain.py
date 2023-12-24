from Encoding.Hex.Hex_decode import hex_decode_plaintext_bytes

number = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
hexstring = hex(number)[2:]
plaintext = hex_decode_plaintext_bytes(hexstring)

print(number)
print(hexstring)
print(plaintext)