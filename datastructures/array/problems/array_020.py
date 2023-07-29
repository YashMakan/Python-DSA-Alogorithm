"""
https://www.geeksforgeeks.org/rearrange-array-alternating-positive-negative-items-o1-extra-space/
Rearrange array in alternating positive & negative items with O(1) extra space | Set 1
Two pointer approach
"""


def rearrange_array(arr):
    positive_idx = 0
    negative_idx = 1
    n = len(arr)

    # Find the first index with the wrong sign to start the swapping process
    while positive_idx < n and negative_idx < n:
        # Find the next positive element
        while positive_idx < n and arr[positive_idx] >= 0:
            positive_idx += 2

        # Find the next negative element
        while negative_idx < n and arr[negative_idx] < 0:
            negative_idx += 2

        # Swap the elements at positive_idx and negative_idx if both are valid
        if positive_idx < n and negative_idx < n:
            arr[positive_idx], arr[negative_idx] = arr[negative_idx], arr[positive_idx]

    return arr


if __name__ == "__main__":
    array = [1, 2, 3, -4, -1, 4]
    print(rearrange_array(array))
