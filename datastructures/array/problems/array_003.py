"""
https://www.geeksforgeeks.org/program-find-minimum-maximum-element-array/
Q: Program to find the minimum (or maximum) element of an array
Example:
    Input: [1, 423, 6, 46, 34, 23, 13, 53, 4]
    Output: min-1, max-423
"""


def find_min_max(arr: list[int]) -> tuple:
    length = arr.__len__()

    if length == 0:
        return -1, -1

    min_value = arr[0]
    max_value = arr[0]

    for i in range(length):
        if arr[i] < min_value:
            min_value = arr[i]
        elif arr[i] > max_value:
            max_value = arr[i]

    return min_value, max_value


if __name__ == "__main__":
    array: list[int] = [1, 423, 6, 46, 34, 23, 13, 53, 4]
    minimum, maximum = find_min_max(array)
    print(f"min-{minimum}, max-{maximum}")
