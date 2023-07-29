"""
https://www.geeksforgeeks.org/count-subarrays-equal-number-1s-0s/
Count subarrays with equal number of 1’s and 0’s

Input: arr[] = {1, 0, 0, 1, 0, 1, 1}
Output: 8
Explanation: The index range for the 8 sub-arrays are: (0, 1), (2, 3), (0, 3), (3, 4), (4, 5)(2, 5), (0, 5), (1, 6)

Input: arr = { 1, 0, 0, 1, 1, 0, 0, 1}
Output: 12

We have to calculate the sum frequency anc make a lookup
"""


def count_subarray_with_equal_number_of_1s_0s(arr: list[int]) -> int:
    current_sum = 0
    # {0: 1} is added because it would exclude the subarray starting from index 0 from being counted.
    current_sum_lookup = {0: 1}
    subarray_count = 0

    for i in range(len(arr)):
        if arr[i] == 0:
            arr[i] = -1

        current_sum += arr[i]

        if current_sum in current_sum_lookup:
            subarray_count += current_sum_lookup[current_sum]
            current_sum_lookup[current_sum] += 1
        else:
            current_sum_lookup[current_sum] = 1

    return subarray_count


if __name__ == "__main__":
    array = [1, 0, 0, 1, 1, 0, 0, 1]
    print(count_subarray_with_equal_number_of_1s_0s(array))

