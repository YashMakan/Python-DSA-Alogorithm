"""
https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/
Write a program to reverse an array or string
Example:
    Input: [1, 2, 3]
    Output: [3, 2, 1]
"""


def reverse_iterative_way(arr: list[int]) -> list[int]:
    length = arr.__len__()
    start = 0
    end = length - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr


def reverse_recursion_way(arr: list[int]) -> list[int]:
    def reverse(ls: list[int], start: int, end: int) -> list:
        if start >= end:
            return ls
        ls[start], ls[end] = ls[end], ls[start]
        return reverse(ls, start + 1, end - 1)
    length = arr.__len__()
    arr = reverse(arr, 0, length - 1)
    return arr


if __name__ == "__main__":
    array: list[int] = [1, 423, 6, 46, 34, 23, 13, 53, 4]
    result: list[int] = reverse_recursion_way(array)
    # result: list[int] = reverse_iterative_way(array)
    print(result)
