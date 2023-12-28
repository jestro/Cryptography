from Encryption.XOR.Helper import data_to_bin7b


def xor(data, key):
    data_bin_list = data_to_bin7b(data)
    key_bin_list = data_to_bin7b(key)

    xor_bin_list = []

    for binary in range(len(data_bin_list)):
        key = key_bin_list[binary % len(key_bin_list)]
        binary = data_bin_list[binary]

        xor_binary = ""

        for number in range(len(binary)):
            if binary[number] == key[number]:
                xor_binary += "0"
            else:
                xor_binary += "1"

        xor_bin_list.append(xor_binary)

    return xor_bin_list
