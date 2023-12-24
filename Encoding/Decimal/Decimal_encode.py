# list or singular item
# format -> c or cry

# plaintext -> decimal
def chr_to_int(plaintext):
    if len(plaintext) == 1:
        return ord(plaintext)

    int_list = []

    for char in plaintext:
        int_list.append(ord(char))

    return int_list

