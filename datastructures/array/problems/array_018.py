"""
https://www.geeksforgeeks.org/non-repeating-element/
Find first non-repeating element in a given Array of integers

Input: {-1, 2, -1, 3, 0}
Output: 2
Explanation: The first number that does not repeat is : 2

Input: {9, 4, 9, 6, 7, 4}
Output: 6

"""


def find_non_repeating_element(arr: list[int]) -> int | None:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    element_counts = {}
    last_element = arr[0]
    for element in arr:
        if element in element_counts:
            element_counts[element] += 1
            if element_counts[element] > 1:
                return last_element
        else:
            element_counts[element] = 1
        last_element = element
    return None


if __name__ == "__main__":
    array = [-1, 10, -12, 3, 0]
    output = find_non_repeating_element(array)
    print(output)