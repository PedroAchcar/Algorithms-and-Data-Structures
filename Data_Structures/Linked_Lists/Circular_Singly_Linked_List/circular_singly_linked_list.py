class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    def length(self):
        """Returns the number of nodes in the circular linked list."""

        if self.head is None:
            return 0

        count = 1
        current = self.head.next

        while current != self.head:
            count += 1
            current = current.next

        return count

    def insert_at_start(self, data):
        """Inserts a node at the beginning of the linked list."""

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.head.next = self.head

        else:
            current = self.head

            while current.next != self.head:
                current = current.next

            current.next = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_at_position(self, data, position: int):
        """Inserts a node at a specific position in the linked list."""

        new_node = Node(data)

        if self.head is None or position == 0:
            self.insert_at_start(data)
            return

        current = self.head
        index = 0

        while current.next != self.head and index < position - 1:
            current = current.next
            index += 1

        new_node.next = current.next
        current.next = new_node

    def insert_at_end(self, data):
        """Inserts a node at the end of the linked list."""

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.head.next = self.head

        else:
            current = self.head

            while current.next != self.head:
                current = current.next

            current.next = new_node
            new_node.next = self.head

    def remove_at_start(self):
        """Removes a node at the beginning of the linked list."""

        if self.head is None:
            print("The linked list is empty.")
            return

        if self.head.next == self.head:
            self.head = None

        else:
            current = self.head

            while current.next != self.head:
                current = current.next

            current.next = self.head.next
            self.head = self.head.next

    def remove_at_position(self, position: int):
        """Removes a node at a specific position in the linked list."""

        if self.head is None:
            print("The linked list is empty.")
            return

        if position == 0:
            self.remove_at_start()
            return

        previous = None
        current = self.head
        index = 0

        while index < position and current.next != self.head:
            previous = current
            current = current.next
            index += 1

        if current == self.head:
            print("Index error: out of range of the linked list.")
            return

        previous.next = current.next

    def remove_at_end(self):
        """Removes a node at the end of the linked list."""

        if self.head is None:
            print("The linked list is empty.")
            return

        if self.head.next == self.head:
            self.head = None

        else:
            previous = None
            current = self.head

            while current.next != self.head:
                previous = current
                current = current.next

            previous.next = self.head

    def print_list(self):
        """Prints the linked list node by node."""

        if self.head is None:
            print("The linked list is empty.")
            return

        current = self.head
        print("[Head] -> ", end="")

        while True:
            print(current.data, "-> ", end='')
            current = current.next

            if current == self.head:
                break

        print("[Back to Head]")

    def search(self, item):
        """Searches an item in the linked list."""

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
    cll = CircularSinglyLinkedList()

    print("\n🔹 Test 1: Insert at the beginning")
    cll.insert_at_start(30)
    cll.insert_at_start(20)
    cll.insert_at_start(10)
    cll.print_list()
    # Expected: [Head] -> 10 -> 20 -> 30 -> [Back to Head]

    print("\n🔹 Test 2: Insert at the end")
    cll.insert_at_end(40)
    cll.insert_at_end(50)
    cll.print_list()
    # Expected: [Head] -> 10 -> 20 -> 30 -> 40 -> 50 -> [Back to Head]

    print("\n🔹 Test 3: Insert at position (index 2)")
    cll.insert_at_position(25, 2)
    cll.print_list()
    # Expected: [Head] -> 10 -> 20 -> 25 -> 30 -> 40 -> 50 -> [Back to Head]

    print("\n🔹 Test 4: Remove from the beginning")
    cll.remove_at_start()
    cll.print_list()
    # Expected: [Head] -> 20 -> 25 -> 30 -> 40 -> 50 -> [Back to Head]

    print("\n🔹 Test 5: Remove from the end")
    cll.remove_at_end()
    cll.print_list()
    # Expected: [Head] -> 20 -> 25 -> 30 -> 40 -> [Back to Head]

    print("\n🔹 Test 6: Remove from position (index 2)")
    cll.remove_at_position(2)
    cll.print_list()
    # Expected: [Head] -> 20 -> 25 -> 40 -> [Back to Head]

    print("\n🔹 Test 7: Search for an existing element (25)")
    found, position = cll.search(25)
    print(
        f"Element 25 {'found' if found else 'not found'} at position {position}")
    # Expected: Element 25 found at position 1

    print("\n🔹 Test 8: Search for a non-existing element (100)")
    found, position = cll.search(100)
    print(
        f"Element 100 {'found' if found else 'not found'} at position {position}")
    # Expected: Element 100 not found at position -1

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
    print(
        f"Element 30 {'found' if found else 'not found'} at position {position}")
    # Expected: Element 30 not found at position -1
