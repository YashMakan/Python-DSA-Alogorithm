"""
Bubble sort is a process of comparing two consecutive elements in an array and sorting till end. This process is
iterated n times when n being the number of elements in the list.
Time complexity: O(n^2)

Pseudocode
for i from 1 to N
    for i from 0 to N - 1
        if a[j] > a[j + 1]
            swap(a[j], a[j + 1])
"""


def bubble_sort(arr: list[int]) -> list[int]:
    length = arr.__len__()
    if length < 2:
        return arr
    for i in range(length):
        for j in range(length - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    array: list[int] = [2, 8, 5, 3, 9, 4, 1]
    array = bubble_sort(array)
    print(array)
