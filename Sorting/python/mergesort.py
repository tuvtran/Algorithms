from typing import List


def mergesort(arr: List[int]) -> List[int]:



if __name__ == "__main__":
    test_arr1 = [10, 2, 3, 4, 5, 3, 8, 11, 4]
    print(mergesort(test_arr1, 0, len(test_arr1)))

    import time
    test_arr2 = list(range(10000, -1, -1))

    start = time.time()
    mergesort(test_arr2, 0, len(test_arr2))
    end = time.time()
    print(end - start)

    start = time.time()
    test_arr2.sort()
    end = time.time()
    print(end - start)
