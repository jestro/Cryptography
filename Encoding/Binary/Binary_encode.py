# list or singular item
# format -> c or cry

# plaintext -> decimal -> binary
def chr_to_bin(plaintext):
    if len(plaintext) == 1:
        return bin(ord(plaintext))

    bin_list = []

    for char in plaintext:
        bin_list.append(bin(ord(char)))

    return bin_list
