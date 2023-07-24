"""
https://www.geeksforgeeks.org/count-number-of-occurrences-or-frequency-in-a-sorted-array/
Count number of occurrences (or frequency) in a sorted array
Example:
    Input: arr[] = {1, 1, 2, 2, 2, 2, 3}, x = 2
    Output: 4

1. Linear search
2. Binary Search
"""


def count_no_of_occurrences_linear_search(arr: list[int], x: int) -> int:
    length = arr.__len__()
    freq = 0
    for i in range(length):
        if arr[i] == x:
            freq += 1
    return freq


def count_no_of_occurrences_binary_search(arr: list[int], x: int) -> int:
    def binary_search_get_first_occurrence(arr1: list[int], x1: int):
        start = 0
        end = arr1.__len__() - 1
        res = -1
        while start <= end:
            mid = (start + end) // 2
            if arr1[mid] > x1:
                end = mid - 1
            elif arr1[mid] < x1:
                start = mid + 1
            else:
                res = mid
                end = mid - 1
        return res

    def binary_search_get_last_occurrence(arr2: list[int], x2: int):
        start = 0
        end = arr2.__len__() - 1
        res = -1
        while start <= end:
            mid = (start + end) // 2
            if arr2[mid] > x2:
                end = mid - 1
            elif arr2[mid] < x2:
                start = mid + 1
            else:
                res = mid
                start = mid + 1
        return res

    oc1 = binary_search_get_first_occurrence(arr, x)
    oc2 = binary_search_get_last_occurrence(arr, x)

    return oc2 - oc1 + 1


if __name__ == "__main__":
    array: list[int] = [2, 5, 7, 8, 9, 12, 14, 14, 14, 14, 18]
    value = 14
    output = count_no_of_occurrences_linear_search(array, value)
    print(output)
    output = count_no_of_occurrences_binary_search(array, value)
    print(output)
