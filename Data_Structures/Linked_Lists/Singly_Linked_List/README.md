# Singly Linked List Implementation in Python

This repository contains an implementation of a **Singly Linked List** in Python. The `SinglyLinkedList` class provides various methods to insert, remove, search, and display nodes efficiently.

## Features
- Insert nodes at the start, end, or at a specific position in the linked list.
- Remove nodes from the start, end, or a specified position.
- Search for a node and retrieve its index.
- Print the linked list in a readable format.

## Class Structure
### `Node`
Represents a node in the linked list.
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

### `SinglyLinkedList`
Manages the linked list operations.
```python
class SinglyLinkedList:
    def __init__(self):
        self.head = None
```

### Methods
#### Insertion Methods
- `insert_at_start(data)`: Inserts a node at the beginning of the list.
- `insert_at_position(data, position)`: Inserts a node at a given position.
- `insert_at_end(data)`: Inserts a node at the end of the list.

#### Deletion Methods
- `remove_at_start()`: Removes the first node.
- `remove_at_position(position)`: Removes the node at a specific position.
- `remove_at_end()`: Removes the last node.

#### Utility Methods
- `print_list()`: Prints the linked list.
- `search(item) -> tuple[bool, int]`: Searches for an item in the linked list.

## Usage
To use this linked list implementation, create an instance of `SinglyLinkedList` and call the available methods as needed.

```python
if __name__ == "__main__":
    singly_linked_list = SinglyLinkedList()
    singly_linked_list.print_list()
    singly_linked_list.remove_at_start()
    singly_linked_list.remove_at_position(3)
    singly_linked_list.remove_at_end()
    print(singly_linked_list.search(2)[0], singly_linked_list.search(2)[1])

    singly_linked_list.insert_at_end(2)
    singly_linked_list.insert_at_end(4)
    singly_linked_list.insert_at_end(5)

    singly_linked_list.print_list()

    singly_linked_list.insert_at_start(1)

    singly_linked_list.print_list()

    singly_linked_list.insert_at_position(3, 2)
    singly_linked_list.insert_at_position(0, 0)

    singly_linked_list.print_list()

    print(singly_linked_list.search(0)[0], singly_linked_list.search(0)[1])
    print(singly_linked_list.search(3)[0], singly_linked_list.search(3)[1])
    print(singly_linked_list.search(7)[0], singly_linked_list.search(7)[1])

    singly_linked_list.remove_at_start()
    singly_linked_list.remove_at_end()

    singly_linked_list.print_list()

    singly_linked_list.remove_at_position(1)

    singly_linked_list.print_list()

    singly_linked_list.remove_at_position(9)

    singly_linked_list.print_list()
```

## Expected Output
```
The linked list is empty.
The linked list is empty.
The linked list is empty.
The linked list is empty.
False -1
2 -> 4 -> 5 -> None
1 -> 2 -> 4 -> 5 -> None
0 -> 1 -> 2 -> 3 -> 4 -> 5 -> None
True 0
True 3
False -1
1 -> 2 -> 3 -> 4 -> None
1 -> 3 -> 4 -> None
Index error: out of range of the linked list.
1 -> 3 -> 4 -> None
```
