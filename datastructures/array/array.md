## What is a Static Array?
A static array is a fixed length container containing n elements `index-able` from the range `[0, n-1]` <br />
PS: `index-able` means that each slot/index can be referenced with a number.

## When & where is Static Array used?
1. Storing and accessing sequential data.
2. Temporarily storing objects.
3. Used by IO routines as buffers
4. Lookup tables and inverse lookup tables.
5. Dynamic programming

## Time Complexity
| Operation        | Static | Dynamic |
|:-----------------|:-------|:--------|
| Access           | O(1)   | O(1)    |
| Search           | O(n)   | O(n)    |
| Insertion        | N/A    | O(n)    |
| Appending        | N/A    | O(1)    |
| Deletion         | N/A    | O(n)    |

## What is Dynamic Array?
The dynamic array can grow and shrink in size. <br />
PS: Dynamic Array can be created using static array.

> The code for the dynamic Array can be found in dynamic_array.py 