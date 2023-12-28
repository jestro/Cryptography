from Encryption.XOR.Helper import data_to_bin7b


def xor(data, key):
    data_bin_list = data_to_bin7b(data)
    key_bin_list = data_to_bin7b(key)

    xor_bin_list = []

    for binary in range(len(data_bin_list)):
        key = key_bin_list[binary % len(key_bin_list)]
        binary = data_bin_list[binary]

        xor_binary = ""

        for bit_index in range(len(binary)):
            xor_binary += xor_gate(binary[bit_index], key[bit_index])

        xor_bin_list.append(xor_binary)

    return xor_bin_list


def xor_gate(bit1, bit2):
    if bit1 == bit2:
        return "0"
    else:
        return "1"
