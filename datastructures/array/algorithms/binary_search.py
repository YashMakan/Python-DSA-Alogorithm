"""
Binary search algorithm is used to search an element in given array but instead of traversing through each element from
left to right. It cuts the array in half from the mid and based on that, it finds the desired element. The algorithm is
only useful for sorted array.
Time Complexity: O(log(n))

"""


def binary_search(arr: list[int], x: int) -> int:
    start = 0
    end = arr.__len__() - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] > x:
            end = mid - 1
        elif arr[mid] < x:
            start = mid + 1
        else:
            return mid
    return -1


def binary_search_get_first_occurrence(arr: list[int], x: int):
    start = 0
    end = arr.__len__() - 1
    res = -1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] > x:
            end = mid - 1
        elif arr[mid] < x:
            start = mid + 1
        else:
            res = mid
            end = mid - 1
    return res


def binary_search_get_last_occurrence(arr: list[int], x: int):
    start = 0
    end = arr.__len__() - 1
    res = -1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] > x:
            end = mid - 1
        elif arr[mid] < x:
            start = mid + 1
        else:
            res = mid
            start = mid + 1
    return res


if __name__ == "__main__":
    array: list[int] = [2, 5, 7, 8, 9, 12, 14, 14, 14, 14, 18]
    value = 14
    result = binary_search(array, value)
    print(result)
    result = binary_search_get_first_occurrence(array, value)
    print(result)
    result = binary_search_get_last_occurrence(array, value)
    print(result)
