def find_smallest(arr):
    smallest = arr[0]
    smallest_idx = 0

    for idx, element in enumerate(arr):
        if element < smallest:
            smallest = element
            smallest_idx = idx

    return smallest_idx

def selection_sort(arr):
    sorted_arr = []

    for i in range(len(arr)):
        smallest = find_smallest(arr)
        sorted_arr.append(arr.pop(smallest))
    return sorted_arr
