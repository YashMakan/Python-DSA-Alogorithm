"""
https://www.geeksforgeeks.org/c-program-cyclically-rotate-array-one/
Program to cyclically rotate an array by one

Input: arr[] = {1, 2, 3, 4, 5}
Output: arr[] = {5, 1, 2, 3, 4}

Input: arr[] = {2, 3, 4, 5, 1}
Output: {1, 2, 3, 4, 5}

"""


def rotate_by_one(arr: list[int]) -> list[int]:
    length = len(arr)
    last_element_index = length - 1
    last_element = arr[last_element_index]
    for i in range(last_element_index, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = last_element
    return arr


if __name__ == "__main__":
    array = [1,45,2,5,6,3]
    print(rotate_by_one(array))