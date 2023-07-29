## What is a Linked list?
A linked list is a sequential list of nodes that hold data which point to other nodes also containing data.<br />
PS: The last node always has null reference.

> DATA ---> DATA ---> DATA ---> NULL

## Where are Linked lists used?
1. Used in many list, Queue & stack implementation.
2. Great for creating circular lists.
3. can easily model real world objects such as trains.
4. Used in separate chaining, which is present certain Hashtable implementations to deal with hashing collisions.
5. Often used in implementation of adjacency lists for graphs.

## Terminology
1. `Head`: The first node in a linked list.
2. `Tail`: the last node in a linked list.
3. `Pointer`: reference to another node(arrow connecting nodes).
4. `Node`: an object containing data and pointer(s).

## Singly vs Doubly Linked List
1. `Singly Linked List` 
   1. Holds the reference to only the next node.
   2. Use less memory.
   3. Simpler implementation.
   4. Cannot easily access previous elements.
2. `Doubly Linked List`
   1. Holds the reference to the next and the previous node.
   2. Use 2x more memory.
   3. Can be traversed backwards.

## Time Complexity
| Operation                 | Singly | Doubly |
|:--------------------------|:-------|:-------|
| Insert at head            | O(1)   | O(1)   |
| Insert at tail            | O(1)   | O(1)   |
| Insert in middle / search | O(n)   | O(n)   |
| Remove at head            | O(1)   | O(1)   |
| Remove at tail            | O(n)   | O(1)   |
| Remove in middle          | O(n)   | O(n)   |
