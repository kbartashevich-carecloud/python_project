def binary_search(list, item):
    """Binary search algorithm"""
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess > item:
            high = mid - 1
        if guess == item:
            return mid
        else:
            low = mid + 1
    return None


my_list = [1, 2, 3, 4, 5, 6, 7, 8]

print(binary_search(my_list, 4))
