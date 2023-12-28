from Encryption.XOR.XOR_decrypt import xor_decrypt

plaintext = "label"
key = 13

print("crypto{" + xor_decrypt(plaintext, key) + "}")
