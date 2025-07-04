from typing import List, Union


def sorter(arr: Union[List[int], List[float]]) -> Union[List[int], List[float]]:
    # Optimized bubble sort: stop early if no swaps
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):  # Don't check the already-sorted end
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
