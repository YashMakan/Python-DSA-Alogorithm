"""
DynamicArray

DynamicArray() -> DynamicArray
    Constructor for creating DynamicArray with default length

DynamicArray(int length) -> DynamicArray
    Constructor for creating DynamicArray with provided length

size() -> int
    Method for getting current size of DynamicArray

is_empty() -> bool
    Method for checking if the array is empty or not

get(int index) -> T
    Method for getting <T> at a specific index

set(int index, T elem) -> void
    Method for set elem<T> at a specific position index and replace

clear() -> void
    Method for clearing all elements from the array

add(T elem) ->
    Method for adding elem<T> at the end of the array

insert(T elem, int index) ->
    Method for inserting elem<T> at a specific index in the array

removeAt(int index) ->
    Method for removing element at specific index from array

remove(T elem) ->
    Method for removing element from array

indexOf(T elem) ->
    Method for returning the index elem in array

contains(T elem) ->
    Method for checking if elem<T> exists in the array

toString() ->
    Method for returning a formatting form of the array in string




PS: We will treat arr property in DynamicArray is a static array
"""
from typing import Any


class DynamicArray:
    def __init__(self, length: int = 2):
        self.capacity = length
        self.length = 0
        self.value = [None] * length

    def size(self) -> int:
        return self.length

    def is_empty(self) -> bool:
        return self.size() == 0

    def get(self, index: int) -> Any:
        return self.value[index]

    def set(self, index: int, elem: Any) -> None:
        self.value[index] = elem

    def clear(self) -> None:
        for index in range(self.capacity):
            self.value[index] = None
        self.length = 0

    def add(self, elem: Any) -> None:
        if self.length + 1 > self.capacity:
            self.capacity *= 2
            arr = [None] * self.capacity
            for i in range(self.length):
                arr[i] = self.value[i]
            self.value = arr
        self.value[self.length] = elem
        self.length += 1

    def insert(self, elem: Any, index: int) -> None:
        if self.length + 1 > self.capacity:
            self.capacity *= 2
            arr = [None] * self.capacity
            for i in range(self.length):
                arr[i] = self.value[i]
            self.value = arr
        for i in range(self.length, index, -1):
            self.value[i] = self.value[i - 1]
        self.value[index] = elem
        self.length += 1

    def remove_at(self, index: int) -> None:
        for i in range(index, self.length - 1):
            self.value[i] = self.value[i + 1]
        self.value[self.length - 1] = None
        self.length -= 1

    def index_of(self, elem: Any) -> int:
        for i in range(len(self.value)):
            if self.value[i] == elem:
                return i
        return -1

    def remove(self, elem: Any) -> None:
        index = self.index_of(elem)
        self.remove_at(index)

    def contains(self, elem: Any) -> bool:
        return self.index_of(elem) != -1

    def to_string(self) -> str:
        text = "["
        for i in range(len(self.value)):
            if self.value[i] is None:
                break
            text += f"{self.value[i]}, "
        text = text.rstrip(", ")
        text += "]"
        return text

    def __str__(self):
        return self.to_string()


if __name__ == "__main__":
    array = DynamicArray()
    array.add(1)
    print(array)
    array.add(2)
    print(array)
    array.add(3)
    print(array)
    array.add(4)
    print(array)
    array.insert(10, 1)
    print(array)
    array.remove_at(2)
    print(array)
    array.remove(4)
    print(array)
    array.clear()
    print(array)
    array.add(1)
    print(array)
