def recursive_binary_search(array: list, target: int, low: int, high: int):
    if low > high:
        return -1

    mid = (low + high) // 2
    if target < array[mid]:
        return recursive_binary_search(array, target, low, mid - 1)
    elif target > array[mid]:
        return recursive_binary_search(array, target, mid + 1, high)
    return mid


def iterative_binary_search(array: list, target):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2

        if array[mid] == target:
            return mid

        if array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
