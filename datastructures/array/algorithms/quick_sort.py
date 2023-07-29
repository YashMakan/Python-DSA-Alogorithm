"""
Quick sort/ Divide and Conquer

Average Time complexity: O(n log(n))
Note: The time complexity/performance depends on the pivot element.

Average case: After first pass, if pivot element is occurring in the middle -> O(n log(n))
Worst Case: If array is already sorted(asc or desc) then the worst case is -> O(n^2)

Rules:
1. Create 3 pointers, v(pivot), p and q
2. Traverse the array and with each iteration, if,
   a. if p < v  -> p++
   b. if q >= v -> q--
3. check,
   a. if p cross over q -> swap(v,q)
      i. split array in two by the pivot and use same algorithm for both
   b. else -> swap(p,q)
      i. continue
4. Once traversed, add all the partitions together

Steps:
v = pivot
p = first index pointer
q = last index pointer
--------------------------------
Partition 1
--------------------------------
35 50 15 25 80 20 90 45 inf
^  ^                  ^
v  P                  q
----
35 50 15 25 80 20 90 45 inf
^  ^           ^
v  P           q
----
35 20 15 25 80 50 90 45 inf
^  ^           ^
v  P           q
----
35 20 15 25 80 50 90 45 inf
^        ^  ^
v        q   p
----
25 50 15 35 80 50 90 45 inf
^        ^  ^
q        v   p
--------------------------------
Partition 2
--------------------------------
25 50 15 inf      80 50 90 45 inf
^  ^  ^           ^  ^     ^
v  p  q           v  p     q
----
25 50 15 inf      80 50 90 45 inf
^     ^  ^        ^     ^  ^
v     q  p        v     p  q
----
15 50 25 inf      80 50 45 90 inf
^     ^  ^        ^     ^  ^
q     v  p        v     q  p
----
15 50 25 inf      45 50 80 90 inf
^     ^  ^        ^     ^  ^
q     v  p        q     v  p
----
[15, 20, 25] + [35] + [45, 50, 80, 90]
----
[15, 20, 25, 35, 45, 60, 80, 90]
--------------------------------
End
--------------------------------
"""


def quick_sort(arr: list[int]) -> list[int]:
    length = arr.__len__()

    return arr


if __name__ == "__main__":
    array: list[int] = [2, 8, 5, 3, 9, 4, 1]
    array = quick_sort(array)
    print(array)
