# Circular Singly Linked List Implementation in Python

This repository contains an implementation of a **Circular Singly Linked List** in Python. The `CircularSinglyLinkedList` class provides various methods to insert, remove, search, and display nodes efficiently.

## Features
- Insert nodes at the start, end, or at a specific position in the linked list.
- Remove nodes from the start, end, or a specified position.
- Search for a node and retrieve its index.
- Print the linked list from head to tail.
- Get the length of the linked list.

## Class Structure
### `Node`
Represents a node in the linked list.
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

### `CircularSinglyLinkedList`
Manages the linked list operations.
```python
class CircularSinglyLinkedList:
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
- `length()`: Returns the number of nodes in the linked list.
- `print_list()`: Prints the linked list from head to tail.
- `search(item) -> tuple[bool, int]`: Searches for an item in the linked list.

## Usage and Test Cases
To use this linked list implementation, create an instance of `CircularSinglyLinkedList` and call the available methods as needed.

```python
if __name__ == "__main__":
    cll = CircularSinglyLinkedList()

    print("\n🔹 Test 1: Insert at the beginning")
    cll.insert_at_start(30)
    cll.insert_at_start(20)
    cll.insert_at_start(10)
    cll.print_list()

    print("\n🔹 Test 2: Insert at the end")
    cll.insert_at_end(40)
    cll.insert_at_end(50)
    cll.print_list()

    print("\n🔹 Test 3: Insert at position (index 2)")
    cll.insert_at_position(25, 2)
    cll.print_list()

    print("\n🔹 Test 4: Remove from the beginning")
    cll.remove_at_start()
    cll.print_list()

    print("\n🔹 Test 5: Remove from the end")
    cll.remove_at_end()
    cll.print_list()

    print("\n🔹 Test 6: Remove from position (index 2)")
    cll.remove_at_position(2)
    cll.print_list()

    print("\n🔹 Test 7: Search for an existing element (25)")
    found, position = cll.search(25)
    print(f"Element 25 {'found' if found else 'not found'} at position {position}")

    print("\n🔹 Test 8: Search for a non-existing element (100)")
    found, position = cll.search(100)
    print(f"Element 100 {'found' if found else 'not found'} at position {position}")

    print("\n🔹 Test 9: Number of nodes")
    print(cll.length())
    # Expected: 3

    print("\n🔹 Test 10: Remove all elements until the list is empty")
    cll.remove_at_start()
    cll.remove_at_start()
    cll.remove_at_start()
    cll.print_list()
    # Expected: The linked list is empty.

    print("\n🔹 Test 11: Search in an empty list")
    found, position = cll.search(30)
    print(f"Element 30 {'found' if found else 'not found'} at position {position}")
    # Expected: Element 30 not found at position -1
```

## Expected Output
```
🔹 Test 1: Insert at the beginning
[Head] -> 10 -> 20 -> 30 -> [Back to Head]

🔹 Test 2: Insert at the end
[Head] -> 10 -> 20 -> 30 -> 40 -> 50 -> [Back to Head]      

🔹 Test 3: Insert at position (index 2)
[Head] -> 10 -> 20 -> 25 -> 30 -> 40 -> 50 -> [Back to Head]

🔹 Test 4: Remove from the beginning
[Head] -> 20 -> 25 -> 30 -> 40 -> 50 -> [Back to Head]

🔹 Test 5: Remove from the end
[Head] -> 20 -> 25 -> 30 -> 40 -> [Back to Head]

🔹 Test 6: Remove from position (index 2)
[Head] -> 20 -> 25 -> 40 -> [Back to Head]

🔹 Test 7: Search for an existing element (25)
Element 25 found at position 1

🔹 Test 8: Search for a non-existing element (100)
Element 100 not found at position -1

🔹 Test 9: Number of nodes
3

🔹 Test 10: Remove all elements until the list is empty
The linked list is empty.

🔹 Test 11: Search in an empty list
Element 30 not found at position -1
```
