import base64

hexstring = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
hexbytes = bytes.fromhex(hexstring)
plaintext = base64.b64encode(hexbytes)

print(hexstring)
print(hexbytes)
print(plaintext)
