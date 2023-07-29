"""
https://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/
Find duplicates in O(n) time and O(1) extra space | Set 1
limit: [0 to n-1]
Tim & Space Complexity: O(N) & O(1)

Steps:
1. Traverse the given array
2. increment the arr[i]%nth element by n
3. return all those indexes i for which arr[i]/n is greater than 1.
PS: arr[i] would be greater than n only if a value “i” has appeared more than once.
"""


def find_duplicates(arr: list[int]) -> list[int]:
    length = len(arr)
    result = []
    for i in range(length):
        x = arr[i] % length
        arr[x] = arr[x] + length
    for i in range(length):
        if arr[i] >= length * 2:
            result.append(i)
    return result


if __name__ == "__main__":
    array = [0, 4, 3, 2, 7, 8, 2, 3, 1]
    print(find_duplicates(array))
