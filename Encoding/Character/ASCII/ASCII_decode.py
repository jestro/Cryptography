# ASCII (if singular) / ASCII list -> plaintext
def ascii_list_to_chr(ascii_list):
    if not isinstance(ascii_list, list):
        return chr(ascii_list)
    else:
        plaintext = ""

        for integer in ascii_list:
            plaintext += chr(integer)

        return plaintext
