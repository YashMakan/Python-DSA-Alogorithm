"""
https://www.geeksforgeeks.org/find-a-peak-in-a-given-array/
Q: Find all peak element indices which is not smaller than its neighbours
Example:
    Input: array[]= {5, 10, 20, 15}
    Output: [2]
    Explanation: The element 20 has neighbors 10 and 15, both of them are less than 20.

    Input: array[] = {10, 20, 15, 2, 23, 90, 67}
    Output: [1, 5]
    Explanation: The element 20 has neighbors 10 and 15, both of them are less than 20, similarly 90 has neighbors 23
                 and 67.
"""


def find_all_peek_greater_element_indices(arr: list[int]) -> list[int]:
    length = arr.__len__()
    result = []

    if length < 1:
        return result
    elif length == 1:
        result.append(0)
        return result
    for i in range(length):
        if i == 0 and arr[i] > arr[i + 1]:
            result.append(i)
        elif i == length - 1 and arr[length - 1] > arr[length - 2]:
            result.append(i)
        elif arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            result.append(i)
    return result


if __name__ == "__main__":
    array: list[int] = [10, 20, 15, 2, 23, 90, 67]
    output = find_all_peek_greater_element_indices(array)
    print(output)
