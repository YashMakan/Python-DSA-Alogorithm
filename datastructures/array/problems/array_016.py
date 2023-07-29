"""
Find common elements in three sorted arrays
ar1[] = {1, 5, 10, 20, 40, 80}
ar2[] = {6, 7, 20, 80, 100}
ar3[] = {3, 4, 15, 20, 30, 70, 80, 120}
Output: 20, 80
"""


def find_common_elements(arr1, arr2, arr3):
    common_elements = []
    i, j, k = 0, 0, 0

    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            common_elements.append(arr1[i])
            i += 1
            j += 1
            k += 1
        elif arr1[i] > arr2[j]:
            j += 1
        elif arr2[j] > arr3[k]:
            k += 1
        else:
            i += 1

    return common_elements


if __name__ == "__main__":
    array1 = [1, 5, 10, 20, 40, 80]
    array2 = [6, 7, 20, 80, 100]
    array3 = [3, 4, 15, 20, 30, 70, 80, 120]

    result = find_common_elements(array1, array2, array3)
    print(result)
