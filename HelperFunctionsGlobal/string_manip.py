def substring(string, start, end):
    return string[start:end]


# Also works on arrays
def split(string, split_amount):
    splitted_string = []

    for index in range(0, len(string), split_amount):
        splitted_string.append(substring(string, index, index + split_amount))

    return splitted_string


def is_string(string):
    return isinstance(string, str)