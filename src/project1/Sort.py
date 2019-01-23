def radix_sort(array, key):
    array.sort(key=key) # todo implement radix sort


def quicksort(array, key):
    _quicksort(array, key, 0, len(array) - 1)


def _quicksort(array, key, lo, hi):
    if lo < hi:
        p = _partition(array, key, lo, hi)
        _quicksort(array, key, lo, p - 1)
        _quicksort(array, key, p + 1, hi)


def _partition(array, key, lo, hi):
    pivot = array[hi]
    i = lo
    for j in range(lo, hi):
        if key(array[j]) < key(pivot):
            _swap(array, i, j)
            i += 1
    _swap(array, i, hi)
    return i


def _swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
