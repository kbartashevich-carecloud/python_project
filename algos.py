def is_unique(string):
    chr_map = dict()

    for chr in string:
        if not chr_map.get(chr, None):
            chr_map[chr] = True
        else:
            return False

    return True

def is_unique_2(string):
    counter = 1

    for chr in string:
        if chr in string[counter:]:
            return False
        else:
            counter += 1

    return True

def is_permutation(str_a="", str_b=""):
    len_a, len_b = len(str_a), len(str_b)

    if len_a == 0 or len_b == 0 or len_a != len_b:
        return False

    if sorted(str_a) == sorted(str_b):
        return True

    return False


def urlify(string=""):
    if not string:
        return string

    return string.strip().replace(" ", "%20")

print(urlify("Mr John Smith    "))
