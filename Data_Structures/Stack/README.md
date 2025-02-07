# Stack Implementation

This repository contains an implementation of a **Stack (LIFO - Last In, First Out)** using a **Singly Linked List**. The `Stack` class provides various methods to push, pop, peek, and check if the stack is empty.


## Features
- Push elements onto the stack.
- Pop elements from the stack.
- Peek at the top element without removing it.
- Check if the stack is empty.
- Check the size of the stack.
- Clear the stack.

## Class Structure
### `Node`
Represents a node in the stack.
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

### `Stack`
Manages the stack operations.
```python
class Stack:
    def __init__(self):
        self.top = None
```

### Methods
#### Stack Operations
- `push(data)`: Pushes an element onto the stack.
- `pop()`: Removes and returns the top element from the stack.
- `peek()`: Returns the top element without removing it.
- `is_empty()`: Checks if the stack is empty.
- `size()`: Returns the size of the stack.
- `clear()`: Clear the stack.

## Usage and Test Cases
To use this stack implementation, create an instance of `Stack` and call the available methods as needed.

```python
if __name__ == "__main__":

    stack = Stack()

    print("\n🔹 Test 1: Push elements onto the stack")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack.peek())
    # Expected: 30

    print("\n🔹 Test 2: Pop element from the stack")
    print(f"Popped element: {stack.pop()}")
    # Expected: Popped element: 30

    print("\n🔹 Test 3: Push more elements and see the top of the stack")
    stack.push(40)
    stack.push(50)
    print(stack.peek())
    # Expected: 50

    print("\n🔹 Test 4: Size of the stack")
    print(stack.size())
    # Expected: 4

    print("\n🔹 Test 5: Pop all elements")
    stack.clear()
    print(f"Is stack empty? {stack.is_empty()}. Number of nodes: {stack.size()}")
    # Expected: Is stack empty? True. Number of nodes: 0

    print("\n🔹 Test 6: Pop from empty stack")
    print(stack.pop())
    # Expected: The stack is empty. None

    print("\n🔹 Test 7: Peek in an empty stack")
    print(stack.peek())
    # Expected: The stack is empty.

    print("\n🔹 Test 8: Size of the stack")
    print(stack.size())
    # Expected: 0
```

## Expected Output
```
🔹 Test 1: Push elements onto the stack
30

🔹 Test 2: Pop element from the stack
Popped element: 30

🔹 Test 3: Push more elements and see the top of the stack
50

🔹 Test 4: Size of the stack
4

🔹 Test 5: Pop all elements
Is stack empty? True. Number of nodes: 0

🔹 Test 6: Pop from empty stack
The stack is empty.
None

🔹 Test 7: Peek in an empty stack
The stack is empty.

🔹 Test 8: Size of the stack
0
```
