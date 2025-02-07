# Deque Implementation

This repository contains an implementation of a **Deque (Double-Ended Queue)** using a **Doubly Linked List**. The `Deque` class provides various methods to insert, remove, peek, and check elements at both ends efficiently.

## Features
- Insert elements at the front and back.
- Remove elements from the front and back.
- Peek at the front and back elements without removing them.
- Check if the deque is empty.
- Check the length of the deque.
- Clear the deque.

## Class Structure
### `Node`
Represents a node in the doubly linked list.
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
```

### `Deque`
Manages the deque operations.
```python
class Deque:
    def __init__(self):
        self.front = None
        self.back = None
        self._length = 0
```

### Methods
#### Deque Operations
- `push_front(data)`: Inserts an element at the front of the deque.
- `push_back(data)`: Inserts an element at the back of the deque.
- `pop_front()`: Removes and returns the first element from the deque.
- `pop_back()`: Removes and returns the last element from the deque.
- `peek_front()`: Returns the first element without removing it.
- `peek_back()`: Returns the last element without removing it.
- `is_empty()`: Checks if the deque is empty.
- `length()`: Returns the number of elements in the deque.
- `clear()`: Clears the deque.

## Usage and Test Cases
To use this deque implementation, create an instance of `Deque` and call the available methods as needed.

```python
if __name__ == "__main__":

    deque = Deque()

    print("\n🔹 Test 1: Push elements to the front and back of the deque")
    deque.push_front(10)
    deque.push_front(20)
    deque.push_back(30)
    deque.push_back(40)
    print(f"Front element: {deque.peek_front()}")
    # Expected: Front element: 20
    print(f"Back element: {deque.peek_back()}")
    # Expected: Back element: 40

    print("\n🔹 Test 2: Pop element from the front")
    print(f"Popped front element: {deque.pop_front()}")
    # Expected: Popped front element: 20

    print("\n🔹 Test 3: Push more elements and check the deque")
    deque.push_front(50)
    deque.push_back(60)
    print(f"Front element: {deque.peek_front()}")
    # Expected: Front element: 50
    print(f"Back element: {deque.peek_back()}")
    # Expected: Back element: 60

    print("\n🔹 Test 4: Length of the deque")
    print(f"Deque size: {deque.length()}")
    # Expected: Deque size: 5

    print("\n🔹 Test 5: Clear all elements")
    deque.clear()
    print(f"Is deque empty? {deque.is_empty()}. Number of elements: {deque.length()}")
    # Expected: Is deque empty? True. Number of elements: 0

    print("\n🔹 Test 6: Pop from front and back an empty deque")
    print(deque.pop_front())
    # Expected: None
    print(deque.pop_back())
    # Expected: None

    print("\n🔹 Test 7: Peek front and back into an empty deque")
    print(deque.peek_front())
    # Expected: None
    print(deque.peek_back())
    # Expected: None

    print("\n🔹 Test 8: Length of the deque")
    print(f"Deque size: {deque.length()}")
    # Expected: Deque size: 0
```

## Expected Output
```
🔹 Test 1: Push elements to the front and back of the deque
Front element: 20
Back element: 40

🔹 Test 2: Pop element from the front
Popped front element: 20

🔹 Test 3: Push more elements and check the deque
Front element: 50
Back element: 60

🔹 Test 4: Length of the deque
Deque size: 5

🔹 Test 5: Clear all elements
Is deque empty? True. Number of elements: 0

🔹 Test 6: Pop from front and back an empty deque
None
None

🔹 Test 7: Peek front and back into an empty deque
None
None

🔹 Test 8: Length of the deque
Deque size: 0
```
