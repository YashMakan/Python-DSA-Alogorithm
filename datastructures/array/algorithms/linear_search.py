"""
Linear search algorithm to find element or element index in a given array by traversing through each element one by one.
Time Complexity: O(n)

Pseudocode:
for element in elements
    if element matches with x
        return element

"""


def linear_search(arr: list[int], x: int) -> int:
    length = arr.__len__()
    for i in range(length):
        if x == arr[i]:
            return i

    return -1


if __name__ == "__main__":
    array: list[int] = [2, 8, 5, 3, 9, 4, 1]
    value = 5
    result = linear_search(array, value)
    print(result)
