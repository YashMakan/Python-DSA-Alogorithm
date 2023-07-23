## Data Structure
A data structure is a way of organizing data so that it can be used effectively.

## Why are Data Structure Important?
1. There are essential ingredients in creating fast and powerful algorithms.
2. They help to manage and organize data.
3. They make code cleaner and easier to understand

## Abstract Data Types vs Data Structure
| Abstraction (ADT) | Implementation (DS)                                                           |
|:------------------|:------------------------------------------------------------------------------|
| `List`            | `Dynamic Array` <br/> `Linked List`                                           |
| `Queue`           | `Linked List based Queue` <br/> `Array based Queue` <br/> `Stack based Queue` |
| `Map`             | `Tree Map` <br/> `Hash Map / Hash Table`                                      |

## Computational Complexity Analysis
> How much time the algorithm takes? <br/>
> How much space the algorithm takes?

### Big O Notation
A standardise way to which gives an upper bound of the complexity in the worst case, helping to quantify performance as the input size becomes arbitrarily large.

| Complexity        | Notation                |
|:------------------|:------------------------|
| Constant time     | O(1)                    |
| Logarithmic time  | O(log(n))               |
| Linear time       | O(n)                    |
| Linearithmic time | O(nlog(n))              |
| Quadric time      | O(n<sup>2</sup>)        |
| Cubic time        | O(n<sup>3</sup>)        |
| Exponential time  | O(b<sup>n</sup>), b > 1 |
| Factorial time    | O(n!)                   |

### Big O Properties
1. for `f(n)` equation, the `O(f(n))` will be always the highest order of time complexity. example,<br />
   **If, f(n) = 7log(n)<sup>3</sup> + 15n<sup>2</sup> + 2n<sup>3</sup> + 8 <br />
   Then, O(f(n)) = O(n<sup>3</sup>)**
2. If `f(n)` does not depend on `n` for the output then the `O(f(n))` will be `Constant time / O(1)`
3. For calculating `O(f(n))` multiply the complexity on different loop levels and add complexity on same loop levels.
