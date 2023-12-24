import base64
from Encoding.Hex.Hex_decode import hex_decode_plaintext_bytes

hexstring = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
string = hex_decode_plaintext_bytes(hexstring)
base64 = base64.b64encode(string)

print(hexstring)
print(string)
print(base64)