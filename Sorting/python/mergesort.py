from typing import List


def mergesort(arr: List[int]) -> List[int]:

    if len(arr) == 1:
        return arr

    mid = len(arr) // 2

    arr1 = mergesort(arr[:mid])
    arr2 = mergesort(arr[mid:])

    return merge(arr1, arr2)


def merge(arr1: List[int], arr2: List[int]) -> List[int]:

    i = j = k = 0
    merged = [0] * (len(arr1) + len(arr2))

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged[k] = arr1[i]
            i += 1
        else:
            merged[k] = arr2[j]
            j += 1
        k += 1

    while i < len(arr1):
        merged[k] = arr1[i]
        i, k = i + 1, k + 1

    while j < len(arr2):
        merged[k] = arr2[j]
        j, k = j + 1, k + 1

    return merged


if __name__ == "__main__":
    test_arr1 = [10, 2, 3, 4, 5, 3, 8, 11, 4]
    print(mergesort(test_arr1))

    import time
    test_arr2 = list(range(10000, -1, -1))

    start = time.time()
    mergesort(test_arr2)
    end = time.time()
    print(end - start)

    start = time.time()
    test_arr2.sort()
    end = time.time()
    print(end - start)
