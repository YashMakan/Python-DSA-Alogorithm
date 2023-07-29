"""
https://www.geeksforgeeks.org/find-first-repeating-element-array-integers/
Find the first repeating element in an array of integers
"""


def find_repeating_element(arr: list[int]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    element_counts = {}
    for element in arr:
        if element in element_counts:
            element_counts[element] += 1
            if element_counts[element] > 1:
                return element
        else:
            element_counts[element] = 1
    return -1


if __name__ == "__main__":
    array = [10, 10, 10, 4, 3, 5, 6]
    print(find_repeating_element(array))
