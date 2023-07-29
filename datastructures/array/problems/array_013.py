"""
https://www.geeksforgeeks.org/count-pairs-with-given-sum/
Count pairs with given sum

Input: arr[] = {1, 5, 7, -1}, K = 6
Output:  2
Explanation: Pairs with sum 6 are (1, 5) and (7, -1).

Input: arr[] = {1, 5, 7, -1, 5}, K = 6
Output:  3
Explanation: Pairs with sum 6 are (1, 5), (7, -1) & (1, 5).

Input: arr[] = {1, 1, 1, 1}, K = 2
Output:  6
Explanation: Pairs with sum 2 are (1, 1), (1, 1), (1, 1), (1, 1), (1, 1).

Input: arr[] = {10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1}, K = 11
Output:  9
Explanation: Pairs with sum 11 are (10, 1), (10, 1), (10, 1), (12, -1), (10, 1), (10, 1), (10, 1), (7, 4), (6, 5).

"""


def count_pairs_with_given_sum(arr: list[int], target: int) -> int:
    freq_dict = {}
    count = 0
    for i in range(len(arr)):
        if target - arr[i] in freq_dict:
            count += freq_dict[target - arr[i]]

        if arr[i] in freq_dict:
            freq_dict[arr[i]] += 1
        else:
            freq_dict[arr[i]] = 1
    return count


if __name__ == "__main__":
    array = [10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1]
    target_sum = 11
    print(count_pairs_with_given_sum(array, target_sum))
