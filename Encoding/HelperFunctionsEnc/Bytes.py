# Will only take hexstrings without "0x" prefix
# "637279" -> b'cry'
def hex_to_plaintext_byte(hexstring):
    return bytes.fromhex(hexstring)


# Will only take bytes
# b'Hello' -> '48656c6c6f'
def plaintext_byte_to_hex(plaintext):
    return plaintext.hex()
