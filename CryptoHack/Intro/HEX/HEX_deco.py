def split(string, split_amount):
    splitted_string = []

    for index in range(0, len(string), split_amount):
        splitted_string.append(string[index:index + split_amount])

    return splitted_string


def hex_to_numbers(hexes):
    hex_values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    hex_eq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    numbers = []

    for hexcode in hexes:
        hexcode = hexcode.upper()
        number = 0

        for index in range(0, len(hexcode)):
            last_index = len(hexcode) - 1
            number += hex_eq[hex_values.index(hexcode[index])] * pow(16, last_index - index)

        numbers.append(number)

    return numbers


# Use ascii deco to decode numbers
