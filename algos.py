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

def palindrome_perm(string=""):
    new_str = string.lower().replace(" ", "")
    found_one = False
    is_odd = None

    if new_str == "":
        return True

    is_odd = len(new_str) % 2 == 0

    letter_map = dict()

    for chr in new_str:
        letter_map[chr] = letter_map.setdefault(chr, 0) + 1

    for key in letter_map:
        val = letter_map[key]

        if not is_odd:

            if val == 1 and not found_one:
                found_one = True
                continue
            elif val == 1 and found_one:
                return False

        if val != 2:
            return False

    return True

print(palindrome_perm("roza a zor"))


