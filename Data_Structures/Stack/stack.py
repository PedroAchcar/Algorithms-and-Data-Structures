class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self._lenght = 0

    def push(self, data):
        """Push a value into the top of the stack."""

        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self._lenght += 1

    def pop(self):
        """Remove and return a value in the top of the stack."""

        if self.top is None:
            print("The stack is empty.")

        else:
            data = self.top.data
            self.top = self.top.next
            self._lenght -= 1
            return data

    def peek(self):
        """Return the top item in the stack."""

        if self.top is None:
            print("The stack is empty.")
            return

        return self.top.data

    def is_empty(self):
        """Return True if the stack is empty, False otherwise."""

        return self.top is None

    def lenght(self):
        """Get the number of items in the stack."""

        return self._lenght

    def clear(self):
        """Clear the stack."""

        self.top = None
        self._lenght = 0


if __name__ == "__main__":

    stack = Stack()

    print("\n🔹 Test 1: Push elements onto the stack")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.peek()
    # Expected: 30

    print("\n🔹 Test 2: Pop element from the stack")
    print(f"Popped element: {stack.pop()}")
    # Expected: Popped element: 30

    print("\n🔹 Test 3: Push more elements and see the top of the stack")
    stack.push(40)
    stack.push(50)
    stack.peek()
    # Expected: 50

    print("\n🔹 Test 4: Lenght of the stack")
    print(stack.lenght())
    # Expected: 4

    print("\n🔹 Test 5: Pop all elements")
    stack.clear()
    print(
        f"Is stack empty? {stack.is_empty()}. Number of nodes: {stack.lenght()}")
    # Expected: Is stack empty? True. Number of nodes: 0

    print("\n🔹 Test 6: Pop from empty stack")
    print(stack.pop())
    # Expected: The stack is empty. None

    print("\n🔹 Test 7: Peek in an empty stack")
    stack.peek()
    # Expected: The stack is empty.

    print("\n🔹 Test 8: Lenght of the stack")
    print(stack.lenght())
    # Expected: 0
