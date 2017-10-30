import random


def quicksort3(arr, l, r):
    if l >= r:
        return

    rand_idx = random.randint(l, r - 1)

    m1, m2 = partition3(arr, l, r, arr[rand_idx])

    quicksort3(arr, l, m1)
    quicksort3(arr, m2 + 1, r)

    return arr


def partition3(arr, lo, hi, n):
    """
        All elements less n will be all the left
        all elements more than n will be all the right
        return the indices of n as a tuple
    """
    i, l, r = lo, lo, hi - 1
    while i <= r:
        if arr[i] < n:
            arr[i], arr[l] = arr[l], arr[i]
            i, l = i + 1, l + 1
        elif arr[i] > n:
            arr[i], arr[r] = arr[r], arr[i]
            r -= 1
        else:
            i += 1

    return l, r


if __name__ == "__main__":
    test_arr1 = [10, 2, 3, 4, 5, 3, 8, 11, 4]
    print(quicksort3(test_arr1, 0, len(test_arr1)))

    import time
    test_arr2 = list(range(10000, -1, -1))

    start = time.time()
    quicksort3(test_arr2, 0, len(test_arr2))
    end = time.time()
    print(end - start)

    start = time.time()
    test_arr2.sort()
    end = time.time()
    print(end - start)
