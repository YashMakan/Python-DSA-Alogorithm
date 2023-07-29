"""
Sliding Window: This algorithm is used for making a sliding window of sub-array. Using Sliding window algorithm, one can
efficiently find the max sum of a fixed window of subarray or find the sub array for a given sum.

Identification:
1. given - Array or string
2. asking - sub array or sub string
3. window size(fixed variation) or condition(variable variation)

Time complexity: O(N)
Space complexity: O(1)

Type of Sliding Window:
_____
    |___ Fixed Variation
    |
    |___ Variable Variation

Sliding window Questions
Q1. From given window size, get max sum in sub arrays.
Q2. From given sum, get all the sub array with sum
"""


# Q1. From given window size, get max sum sub array in sub arrays. -> nested loop
def get_max_sum_in_sub_arrays_fixed_variation_nested_loop(arr: list[int], w_size: int) -> int:
    length = arr.__len__()
    start = 0
    end = w_size - 1
    result = -1
    while end < length:
        res = sum(arr[start:end + 1])
        if result < res:
            result = res
        start += 1
        end += 1
    return result


# Q1. From given window size, get max sum sub array in sub arrays. -> sliding window
def get_max_sum_in_sub_arrays_fixed_variation_sliding_window(arr: list[int], w_size: int) -> int:
    length = arr.__len__()
    start = 0
    end = w_size - 1
    curr_sub_arr = sum(arr[start:end + 1])
    sum_array = [curr_sub_arr]
    for i in range(length - w_size):
        curr_sub_arr = curr_sub_arr - arr[i]
        curr_sub_arr = curr_sub_arr + arr[i + w_size]
        sum_array.append(curr_sub_arr)
    return max(sum_array)


# Q2. From given sum, get first sub array. -> sliding window
def get_sub_array_from_max_sum_in_sub_arrays_variable_variation_sliding_window(arr: list[int], sum_value: int) -> tuple:
    """
    Initialize two pointers, start and end, both pointing to the first element of the array.

    Initialize a variable current_sum to the value of the first element of the array.

    Start a loop, and in each iteration, check if current_sum is

    1. equal to target sum, you have found the subarray with the given sum. Return the indices start and end.
    2. If it is less than the target sum, move the end pointer to the right and update current_sum by adding the element
       at the new end index.
    3. If it is greater than the target sum, move the start pointer to the right and subtract the element at the old
       start index from current_sum.

    """
    length = arr.__len__()
    start = 0
    end = w_size - 1
    curr_sub_arr = sum(arr[start:end + 1])
    sum_array = [curr_sub_arr]
    for i in range(length - w_size):
        curr_sub_arr = curr_sub_arr - arr[i]
        curr_sub_arr = curr_sub_arr + arr[i + w_size]
        sum_array.append(curr_sub_arr)
    return max(sum_array)


if __name__ == "__main__":
    array: list[int] = [1, 4, 7, 4, 8, 4, 8, 4]
    window_size = 3

    # output = get_max_sum_in_sub_arrays_fixed_variation_nested_loop(array, window_size)

    output = get_max_sum_in_sub_arrays_fixed_variation_sliding_window(array, window_size)

    print(output)
