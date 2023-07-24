"""
https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/
Sort an array of 0s, 1s and 2s | Dutch National Flag problem

- The Dutch national flag (DNF) problem is one of the most popular programming problems proposed by Edsger Dijkstra.
- The flag of the Netherlands consists of three colors: white, red, and blue. The task is to randomly arrange balls of
  white, red, and blue such that balls of the same color are placed together.

The problem is as follows:

input:  [0, 1, 2, 0, 1, 2]
output: [0, 0, 1, 1, 2, 2]

Time Complexity: O(N)
Space Complexity: O(1)

rules:
1. Elements <- left of the low will always be 0
2. Elements -> right of the high will always 2
3. With each traverse,
    if mid = 1 -> increment mid
    if mid = 0 -> swap(low, mid) + increment low and mid
    if mid = 2 -> swap(high, mid) + decrement high

"""


def dnf(arr: list[int]) -> list[int]:
    length = arr.__len__()
    low = 0
    mid = 0
    high = length - 1
    for i in range(length):
        if arr[mid] == 1:
            mid += 1
        elif arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 2:
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1
        else:
            raise Exception("Only elements with 0s, 1s and 2s are allowed")
    return arr


if __name__ == "__main__":
    array: list[int] = [1, 0, 2, 0, 1, 2, 2, 2, 1, 0, 0, 1]
    print(dnf(array))
