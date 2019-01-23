import math


def binary_search(array, item, key):
    """
    Searches the specified array using the binary search algorithm.
    :param array: the array to search
    :param item: the item you are looking for
    :param key: lambda to specify the property of the object you are checking
    :return: the index of the item if found. -1 otherwise.
    """
    left = 0
    right = len(array) - 1
    while left <= right:
        m = int(math.floor((left + right) / 2))
        if key(array[m]) == item:
            return m
        elif key(array[m]) < item:
            left = m + 1
        elif key(array[m]) > item:
            right = m - 1
    return -1


def sequential_search(array, item, key):
    """
    Searches the specified array using the linear search algorithm.
    :param array: the array to search
    :param item: the item you are looking for
    :param key: lambda to specify the property of the object you are checking
    :return: the index of the item if found. -1 otherwise.
    """
    for i in range(0, len(array)):
        if key(array[i]) == item:
            return i
    return -1
