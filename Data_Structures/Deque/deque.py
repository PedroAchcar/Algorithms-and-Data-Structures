class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.front = None
        self.back = None
        self._length = 0

    def push_front(self, data):
        """Inserts a node at the front of the deque."""

        new_node = Node(data)

        if self.front is None:
            self.front = new_node
            self.back = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node

        self._length += 1

    def push_back(self, data):
        """Inserts a node at the back of the deque."""

        new_node = Node(data)

        if self.back is None:
            self.front = new_node
            self.back = new_node
        else:
            new_node.prev = self.back
            self.back.next = new_node
            self.back = new_node

        self._length += 1

    def pop_front(self):
        """Removes and returns a node from the front of the deque."""

        if self.front is None:
            return None

        data = self.front.data

        if self.front == self.back:
            self.front = None
            self.back = None
        else:
            self.front = self.front.next
            self.front.prev = None

        self._length -= 1

        return data

    def pop_back(self):
        """Removes and returns a node from the back of the deque."""

        if self.back is None:
            return None

        data = self.back.data

        if self.front == self.back:
            self.front = None
            self.back = None
        else:
            self.back = self.back.prev
            self.back.next = None

        self._length -= 1
        return data

    def peek_front(self):
        """Returns the front element without removing it."""

        if self.front is None:
            return None

        else:
            return self.front.data

    def peek_back(self):
        """Returns the back element without removing it."""

        if self.back is None:
            return None

        else:
            return self.back.data

    def is_empty(self):
        """Checks if the deque is empty."""

        return self.front is None

    def length(self):
        """Returns the number of nodes in the deque."""

        return self._length

    def clear(self):
        """Clears the deque."""

        self.front = None
        self.back = None
        self._length = 0


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
    print(
        f"Is deque empty? {deque.is_empty()}. Number of elements: {deque.length()}")
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
