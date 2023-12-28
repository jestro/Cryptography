# Only possible if decimals are ASCII
# decimal -> plaintext
def ascii_array_to_chr(ascii_list):
    if isinstance(ascii_list, int):
        return chr(ascii_list)
    else:
        plaintext = ""

        for integer in ascii_list:
            plaintext += chr(integer)

        return plaintext
