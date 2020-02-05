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

