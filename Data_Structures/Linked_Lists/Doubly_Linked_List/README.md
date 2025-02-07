# Doubly Linked List Implementation in Python

This repository contains an implementation of a **Doubly Linked List** in Python. The `DoublyLinkedList` class provides various methods to insert, remove, search, and display nodes efficiently.

## Features
- Insert nodes at the start, end, or at a specific position in the linked list.
- Remove nodes from the start, end, or a specified position.
- Search for a node and retrieve its index.
- Print the linked list in forward and reverse order.

## Class Structure
### `Node`
Represents a node in the linked list.
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

### `DoublyLinkedList`
Manages the linked list operations.
```python
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
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
- `print_from_head_to_tail()`: Prints the linked list from head to tail.
- `print_from_tail_to_head()`: Prints the linked list from tail to head.
- `search(item) -> tuple[bool, int]`: Searches for an item in the linked list.

## Usage and Test Cases
To use this linked list implementation, create an instance of `DoublyLinkedList` and call the available methods as needed.

```python
if __name__ == "__main__":

    dll = DoublyLinkedList()

    print("\n🔹 Test 1: Insert at the beginning")
    dll.insert_at_start(30)
    dll.insert_at_start(20)
    dll.insert_at_start(10)
    dll.print_from_head_to_tail()
    # Expected: None <-> 10 <-> 20 <-> 30 <-> None

    print("\n🔹 Test 2: Insert at the end")
    dll.insert_at_end(40)
    dll.insert_at_end(50)
    dll.print_from_head_to_tail()
    # Expected: None <-> 10 <-> 20 <-> 30 <-> 40 <-> 50 <-> None

    print("\n🔹 Test 3: Insert at position (index 2)")
    dll.insert_at_position(25, 2)
    dll.print_from_head_to_tail()
    # Expected: None <-> 10 <-> 20 <-> 25 <-> 30 <-> 40 <-> 50 <-> None

    print("\n🔹 Test 4: Print in reverse order (tail -> head)")
    dll.print_from_tail_to_head()
    # Expected: None <-> 50 <-> 40 <-> 30 <-> 25 <-> 20 <-> 10 <-> None

    print("\n🔹 Test 5: Remove from the beginning")
    dll.remove_at_start()
    dll.print_from_head_to_tail()
    # Expected: None <-> 20 <-> 25 <-> 30 <-> 40 <-> 50 <-> None

    print("\n🔹 Test 6: Remove from the end")
    dll.remove_at_end()
    dll.print_from_head_to_tail()
    # Expected: None <-> 20 <-> 25 <-> 30 <-> 40 <-> None

    print("\n🔹 Test 7: Remove from position (index 2)")
    dll.remove_at_position(2)
    dll.print_from_head_to_tail()
    # Expected: None <-> 20 <-> 25 <-> 40 <-> None

    print("\n🔹 Test 8: Search for an existing element (25)")
    found, position = dll.search(25)
    print(f"Element 25 {'found' if found else 'not found'} at position {position}")
    # Expected: Element 25 found at position 1

    print("\n🔹 Test 9: Search for a non-existing element (100)")
    found, position = dll.search(100)
    print(f"Element 100 {'found' if found else 'not found'} at position {position}")
    # Expected: Element 100 not found at position -1

    print("\n🔹 Test 10: Remove from an out-of-range position (index 10)")
    dll.remove_at_position(10)
    # Expected: "Index error: out of range of the linked list."

    print("\n🔹 Test 11: Number of nodes")
    print(dll.lenght())
    # Expected: 3

    print("\n🔹 Test 11: Remove all elements until the list is empty")
    dll.remove_at_start()
    dll.remove_at_start()
    dll.remove_at_start()
    dll.print_from_head_to_tail()
    # Expected: The linked list is empty.

    print("\n🔹 Test 12: Search in an empty list")
    found, position = dll.search(30)
    print(f"Element 30 {'found' if found else 'not found'} at position {position}")
    # Expected: Element 30 not found at position -1
```

## Expected Output
```
🔹 Test 1: Insert at the beginning
None <-> 10 <-> 20 <-> 30 <-> None

🔹 Test 2: Insert at the end
None <-> 10 <-> 20 <-> 30 <-> 40 <-> 50 <-> None       

🔹 Test 3: Insert at position (index 2)
None <-> 10 <-> 20 <-> 25 <-> 30 <-> 40 <-> 50 <-> None

🔹 Test 4: Print in reverse order (tail -> head)       
None <-> 50 <-> 40 <-> 30 <-> 25 <-> 20 <-> 10 <-> None

🔹 Test 5: Remove from the beginning
None <-> 20 <-> 25 <-> 30 <-> 40 <-> 50 <-> None

🔹 Test 6: Remove from the end
None <-> 20 <-> 25 <-> 30 <-> 40 <-> None

🔹 Test 7: Remove from position (index 2)
None <-> 20 <-> 25 <-> 40 <-> None

🔹 Test 8: Search for an existing element (25)
Element 25 found at position 1

🔹 Test 9: Search for a non-existing element (100)
Element 100 not found at position -1

🔹 Test 10: Remove from an out-of-range position (index 10)
Index error: out of range of the linked list.

🔹 Test 11: Number of nodes
3

🔹 Test 11: Remove all elements until the list is empty
The linked list is empty.

🔹 Test 12: Search in an empty list
Element 30 not found at position -1
```
