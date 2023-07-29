"""
https://www.geeksforgeeks.org/move-negative-numbers-beginning-positive-end-constant-extra-space/
Move all negative numbers to beginning and positive to end with constant extra space

Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
Output: -12 -13 -5 -7 -3 -6 11 6 5

Steps:
1. -ve  -ve -> l++
2. +ve  +ve -> r--
3. +ve  -ve -> swap && l++ && r--
4. -ve  +ve -> l++ && r--
"""


def reorder(arr: list[int]) -> list[int]:
    length = arr.__len__()
    start = 0
    end = length - 1
    while start < end:
        if arr[start] < 0 and arr[end] < 0:
            start += 1
        elif arr[start] >= 0 and arr[end] >= 0:
            end -= 1
        elif arr[start] >= 0 and arr[end] < 0:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        else:
            start += 1
            end -= 1
    return arr


if __name__ == "__main__":
    array: list[int] = [-1, -3, -5, 1, 2, 5, 1 - 2, -3, -6, 1, -1, 3]
    print(reorder(array))
