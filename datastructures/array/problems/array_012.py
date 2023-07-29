"""
https://www.geeksforgeeks.org/find-the-missing-number/
Find the Missing Number

Input: arr[] = {1, 2, 4, 6, 3, 7, 8}, N = 8
Output: 5
Explanation: The missing number between 1 to 8 is 5

Input: arr[] = {1, 2, 3, 5}, N = 5
Output: 4
Explanation: The missing number between 1 to 5 is 4

Steps:
1. Create a variable sum = 1 which will store the missing number and a counter variable c = 2.
2. Traverse the array from start to end.
        Update the value of sum as sum = sum – array[i] + c and increment c by 1. This performs the task mentioned in
        the above idea

"""


def find_the_missing_nuber(arr: list[int]) -> int:
    length = len(arr)
    total = (length + 1) * (length + 2) / 2
    arr_sum = sum(arr)
    return int(total - arr_sum)


if __name__ == "__main__":
    array = [1, 2, 4, 5]
    print(find_the_missing_nuber(array))
