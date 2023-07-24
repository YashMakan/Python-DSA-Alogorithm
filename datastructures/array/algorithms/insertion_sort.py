"""
insertion sort is a process of comparing the current element with the left elements and placing the current element
accordingly.
Time complexity: O(n^2) example when array is in descending order

Pseudocode
for i from 1 to N
    while a[i - 1] > a[i]:
        swap(a[i - 1], a[i])
        --i
"""


def insertion_sort(arr: list[int]) -> list[int]:
    length = arr.__len__()
    for i in range(1, length):
        while i > 0 and arr[i - 1] > arr[i]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i = i - 1
    return arr


if __name__ == "__main__":
    array: list[int] = [2, 8, 5, 3, 9, 4, 1]
    array = insertion_sort(array)
    print(array)
