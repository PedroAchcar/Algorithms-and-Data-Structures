# Queue Implementation

This repository contains an implementation of a **Queue (FIFO - First In, First Out)** using a **Singly Linked List**. The `Queue` class provides various methods to enqueue, dequeue, peek, and check if the queue is empty.

## Features
- Enqueue elements into the queue.
- Dequeue elements from the queue.
- Peek at the front element without removing it.
- Check if the queue is empty.
- Check the length of the queue.
- Clear the queue.

## Class Structure
### `Node`
Represents a node in the queue.
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

### `Queue`
Manages the queue operations.
```python
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._length = 0
```

### Methods
#### Queue Operations
- `enqueue(data)`: Inserts an element at the end of the queue.
- `dequeue()`: Removes and returns the first element from the queue.
- `peek()`: Returns the first element without removing it.
- `is_empty()`: Checks if the queue is empty.
- `length()`: Returns the length of the queue.
- `clear()`: Clears the queue.

## Usage and Test Cases
To use this queue implementation, create an instance of `Queue` and call the available methods as needed.

```python
if __name__ == "__main__":

    queue = Queue()

    print("\n🔹 Test 1: Enqueue elements into the queue")
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(f"Front element: {queue.peek()}")
    # Expected: Front element: 10

    print("\n🔹 Test 2: Dequeue element from the queue")
    print(f"Dequeued element: {queue.dequeue()}")
    # Expected: Dequeued element: 10

    print("\n🔹 Test 3: Enqueue more elements and check the front of the queue")
    queue.enqueue(40)
    queue.enqueue(50)
    print(f"Front element: {queue.peek()}")
    # Expected: Front element: 20

    print("\n🔹 Test 4: Length of the queue")
    print(f"Queue size: {queue.length()}")
    # Expected: Queue size: 4

    print("\n🔹 Test 5: Dequeue all elements")
    print(f"Is queue empty? {queue.is_empty()}. Number of elements: {queue.length()}")
    # Expected: Is queue empty? False. Number of elements: 4
    print("Clear the queue.")
    queue.clear()
    print(f"Is queue empty? {queue.is_empty()}. Number of elements: {queue.length()}")
    # Expected: Is queue empty? True. Number of elements: 0

    print("\n🔹 Test 6: Dequeue from an empty queue")
    print(queue.dequeue())
    # Expected: The queue is empty. None

    print("\n🔹 Test 7: Peek into an empty queue")
    print(queue.peek())
    # Expected: The queue is empty. None

    print("\n🔹 Test 8: Length of the queue")
    print(f"Queue size: {queue.length()}")
    # Expected: Queue size: 0
```

## Expected Output
```
🔹 Test 1: Enqueue elements into the queue
Front element: 10

🔹 Test 2: Dequeue element from the queue
Dequeued element: 10

🔹 Test 3: Enqueue more elements and check the front of the queue
Front element: 20

🔹 Test 4: Length of the queue
Queue size: 4

🔹 Test 5: Dequeue all elements
Is queue empty? False. Number of elements: 4
Clear the queue.
Is queue empty? True. Number of elements: 0

🔹 Test 6: Dequeue from an empty queue
The queue is empty.
None

🔹 Test 7: Peek into an empty queue
The queue is empty.
None

🔹 Test 8: Length of the queue
Queue size: 0
```
