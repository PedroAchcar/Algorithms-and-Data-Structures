class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def length(self):
        """Returns the number of nodes in the circular linked list."""

        if self.head is None:
            return 0

        current = self.head
        index = 1

        while current.next != self.head:
            current = current.next
            index += 1

        return index

    def insert_at_start(self, data):
        """Inserts a node at the beginning of the circular linked list."""

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.head.next = self.head
            self.head.prev = self.tail

        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.tail.next = new_node
            self.head.prev = new_node
            self.head = new_node

    def insert_at_position(self, data, position: int):
        """Inserts a node at a specific position in the circular linked list."""

        if position == 0:
            self.insert_at_start(data)
            return

        new_node = Node(data)
        current = self.head
        index = 0

        while index < position - 1 and current.next != self.head:
            current = current.next
            index += 1

        new_node.next = current.next
        new_node.prev = current
        current.next.prev = new_node
        current.next = new_node

        if current == self.tail:
            self.tail = new_node

    def insert_at_end(self, data):
        """Inserts a node at the end of the circular linked list."""

        if self.head is None:
            self.insert_at_start(data)

        else:
            new_node = Node(data)
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node

    def remove_at_start(self):
        """Removes the first node from the circular linked list."""

        if self.head is None:
            print("The linked list is empty.")
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None

        else:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head

    def remove_at_position(self, position: int):
        """Removes a node at a specific position in the circular linked list."""

        if self.head is None:
            print("The linked list is empty.")
            return

        if position == 0:
            self.remove_at_start()
            return

        current = self.head
        index = 0

        while index < position:
            current = current.next
            index += 1

            if current == self.head:
                print("Index error: out of range of the linked list.")
                return

        if current == self.tail:
            self.tail = current.prev

        current.prev.next = current.next
        current.next.prev = current.prev

    def remove_at_end(self):
        """Removes the last node from the circular linked list."""

        if self.head is None:
            print("The linked list is empty.")
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None

        else:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail

    def print_from_head_to_tail(self):
        """Prints the linked list from the head to the tail."""

        if self.head is None:
            print("The linked list is empty.")
            return

        current = self.head
        print("[Head] <-> ", end="")

        while True:
            print(current.data, "<-> ", end="")
            current = current.next

            if current == self.head:
                break

        print("[Back to Head]")

    def print_from_tail_to_head(self):
        """Prints the linked list from the tail to the head."""

        if self.tail is None:
            print("The linked list is empty.")
            return

        current = self.tail
        print("[Tail] <-> ", end="")

        while True:
            print(current.data, "<-> ", end="")
            current = current.prev

            if current == self.tail:
                break

        print("[Back to Tail]")

    def search(self, item) -> tuple[bool, int]:
        """Searches an item in the circular linked list."""

        if self.head is None:
            return False, -1

        current = self.head
        index = 0

        while True:
            if current.data == item:
                return True, index
            current = current.next
            index += 1

            if current == self.head:
                break

        return False, -1


if __name__ == "__main__":

    cll = CircularDoublyLinkedList()

    print("\n🔹 Test 1: Insert at the beginning")
    cll.insert_at_start(30)
    cll.insert_at_start(20)
    cll.insert_at_start(10)
    cll.print_from_head_to_tail()
    # Expected: Head <-> 10 <-> 20 <-> 30 <-> [Back to Head]

    print("\n🔹 Test 2: Insert at the end")
    cll.insert_at_end(40)
    cll.insert_at_end(50)
    cll.print_from_head_to_tail()
    # Expected: Head <-> 10 <-> 20 <-> 30 <-> 40 <-> 50 <-> [Back to Head]

    print("\n🔹 Test 3: Insert at position (index 2)")
    cll.insert_at_position(25, 2)
    cll.print_from_head_to_tail()
    # Expected: Head <-> 10 <-> 20 <-> 25 <-> 30 <-> 40 <-> 50 <-> [Back to Head]

    print("\n🔹 Test 4: Print in reverse order (tail -> head)")
    cll.print_from_tail_to_head()
    # Expected: Tail <-> 50 <-> 40 <-> 30 <-> 25 <-> 20 <-> 10 <-> (Back to Tail)

    print("\n🔹 Test 5: Remove from the beginning")
    cll.remove_at_start()
    cll.print_from_head_to_tail()
    # Expected: Head <-> 20 <-> 25 <-> 30 <-> 40 <-> 50 <-> [Back to Head]

    print("\n🔹 Test 6: Remove from the end")
    cll.remove_at_end()
    cll.print_from_head_to_tail()
    # Expected: Head <-> 20 <-> 25 <-> 30 <-> 40 <-> [Back to Head]

    print("\n🔹 Test 7: Remove from position (index 2)")
    cll.remove_at_position(2)
    cll.print_from_head_to_tail()
    # Expected: Head <-> 20 <-> 25 <-> 40 <-> [Back to Head]

    print("\n🔹 Test 8: Search for an existing element (25)")
    found, position = cll.search(25)
    print(
        f"Element 25 {'found' if found else 'not found'} at position {position}")
    # Expected: Element 25 found at position 1

    print("\n🔹 Test 9: Search for a non-existing element (100)")
    found, position = cll.search(100)
    print(
        f"Element 100 {'found' if found else 'not found'} at position {position}")
    # Expected: Element 100 not found at position -1

    print("\n🔹 Test 10: Remove from an out-of-range position (index 10)")
    cll.remove_at_position(10)
    # Expected: "Index error: out of range of the linked list."

    print("\n🔹 Test 11: Number of nodes")
    print(cll.length())
    # Expected: 3

    print("\n🔹 Test 12: Remove all elements until the list is empty")
    cll.remove_at_start()
    cll.remove_at_start()
    cll.remove_at_start()
    cll.print_from_head_to_tail()
    # Expected: The linked list is empty.

    print("\n🔹 Test 13: Search in an empty list")
    found, position = cll.search(30)
    print(
        f"Element 30 {'found' if found else 'not found'} at position {position}")
    # Expected: Element 30 not found at position -1
