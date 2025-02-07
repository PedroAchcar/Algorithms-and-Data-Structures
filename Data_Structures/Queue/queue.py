class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._length = 0

    def enqueue(self, data):
        """Inserts a new node at the end of the queue."""

        new_node = Node(data)

        if self.rear is None:
            self.front = new_node
            self.rear = new_node

        else:
            self.rear.next = new_node
            self.rear = new_node

        self._length += 1

    def dequeue(self):
        """Removes and returns the first node in the queue."""

        if self.front is None:
            print("The queue is empty.")
            return None

        data = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        self._length -= 1
        return data

    def peek(self):
        """Returns the first element without removing it."""

        if self.front is None:
            print("The queue is empty.")

            return None

        return self.front.data

    def is_empty(self):
        """Checks if the queue is empty."""

        return self.front is None

    def length(self):
        """Returns the number of elements in the queue."""

        return self._length

    def clear(self):
        """Clears the queue."""

        self.front = None
        self.rear = None
        self._length = 0


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
    print(
        f"Is queue empty? {queue.is_empty()}. Number of elements: {queue.length()}")
    # Expected: Is queue empty? False. Number of elements: 4
    print("Clear the queue.")
    queue.clear()
    print(
        f"Is queue empty? {queue.is_empty()}. Number of elements: {queue.length()}")
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
