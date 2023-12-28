from Encryption.XOR.XOR_cipher import xor_cipher

plaintext = "label"
key = 13

print("crypto{" + xor_cipher(plaintext, key, "str") + "}")
