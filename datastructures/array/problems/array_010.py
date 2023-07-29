"""

https://www.geeksforgeeks.org/union-and-intersection-of-two-sorted-arrays-2/
Union and Intersection of two sorted arrays

Input: arr1[] = {1, 3, 4, 5, 7}
        arr2[] = {2, 3, 5, 6}
Output: Union : {1, 2, 3, 4, 5, 6, 7}
         Intersection : {3, 5}

Input: arr1[] = {2, 5, 6}
        arr2[] = {4, 6, 8, 10}
Output: Union : {2, 4, 5, 6, 8, 10}
         Intersection : {6}

union steps:
1. i = 0, j = 0
2. arr[i] < arr[j] -> output.add(arr[i]) && i++
3. arr[i] > arr[j] -> output.add(arr[j]) && j++
4. arr[i] == arr[j] -> i++ && j ++

intersection steps:
1. i = 0, j = 0
2. arr[i] < arr[j] -> i++
3. arr[i] > arr[j] -> j++
4. arr[i] = arr[j] -> i++ && j++
"""


def find_union_and_intersection_of_two_sorted_array(arr1: list[int], arr2: list[int]) -> tuple[list[int], list[int]]:
    union: list[int] = []
    intersection: list[int] = []
    p1 = 0
    p2 = 0

    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] < arr2[p2]:
            union.append(arr1[p1])
            p1 += 1
        elif arr1[p1] > arr2[p2]:
            union.append(arr2[p2])
            p2 += 1
        else:
            union.append(arr1[p1])
            intersection.append(arr1[p1])
            p1 += 1
            p2 += 1

    while p1 < len(arr1):
        union.append(arr1[p1])
        p1 += 1

    while p2 < len(arr2):
        union.append(arr2[p2])
        p2 += 1

    return union, intersection


if __name__ == "__main__":
    array1 = [1, 3, 4, 5, 7]
    array2 = [2, 3, 5, 6, 9]
    u, i = find_union_and_intersection_of_two_sorted_array(array1, array2)
    print(u, i)

