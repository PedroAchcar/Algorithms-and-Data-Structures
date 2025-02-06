class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def lenght(self):
        """Returns the number of nodes in the linked list."""

        current = self.head
        index = 0

        while current is not None:
            current = current.next
            index += 1

        return index

    def insert_at_start(self, data):
        """Inserts a node at the beginning of the linked list."""

        if self.head is None:
            self.head = Node(data)

        else:
            aux = self.head
            self.head = Node(data)
            self.head.next = aux

    def insert_at_position(self, data, position: int):
        """Inserts a node at a specific position in the linked list. 
        If the position is greater than the length of the linked list, 
        the node will be appended at the end of it."""

        new_node = Node(data)

        if position == 0:
            self.insert_at_start(data)
            return

        previous = None
        current = self.head
        index = 0

        while index < position and current is not None:
            previous = current
            current = current.next
            index += 1

        if previous is not None:
            previous.next = new_node
            new_node.next = current

        else:
            self.head = new_node

    def insert_at_end(self, data):
        """Inserts a node at the end of the linked list."""

        if self.head is None:
            self.head = Node(data)

        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = Node(data)

    def remove_at_start(self):
        """Removes a node at the beginning of the linked list."""

        if self.head is None:
            print("The linked list is empty.")

        else:
            self.head = self.head.next

    def remove_at_position(self, position: int):
        """Removes a node at a specific position in the linked list. 
        If the position is greater than the length of the linked list, 
        an error message will be displayed."""

        if self.head is None:
            print("The linked list is empty.")
            return

        if position == 0:
            self.remove_at_start()
            return

        previous = None
        current = self.head
        index = 0

        while index < position and current is not None:
            previous = current
            current = current.next
            index += 1

        if current is None:
            print("Index error: out of range of the linked list.")
            return

        previous.next = current.next

    def remove_at_end(self):
        """Removes a node at the end of the linked list."""

        if self.head is None:
            print("The linked list is empty.")

        else:
            previous = None
            current = self.head

            while current.next is not None:
                previous = current
                current = current.next

            previous.next = None

    def print_list(self):
        """Prints the linked list node by node."""

        if self.head is None:
            print("The linked list is empty.")

        else:
            current = self.head

            while current:
                print(current.data, "-> ", end='')
                current = current.next

            print("None")

    def search(self, item) -> tuple[bool, int]:
        """Searchs an item in the linked list.
        If the linked list has two copies of the item, just the first one will be returned."""

        if self.head is not None:

            current = self.head
            index = 0

            while current:
                if current.data == item:
                    return True, index

                current = current.next
                index += 1

        return False, -1


if __name__ == "__main__":

    sll = SinglyLinkedList()

    print("\n🔹 Test 1: Insert at the beginning")
    sll.insert_at_start(30)
    sll.insert_at_start(20)
    sll.insert_at_start(10)
    sll.print_list()
    # Expected: 10 -> 20 -> 30 -> None

    print("\n🔹 Test 2: Insert at the end")
    sll.insert_at_end(40)
    sll.insert_at_end(50)
    sll.print_list()
    # Expected: 10 -> 20 -> 30 -> 40 -> 50 -> None

    print("\n🔹 Test 3: Insert at position (index 2)")
    sll.insert_at_position(25, 2)
    sll.print_list()
    # Expected: 10 -> 20 -> 25 -> 30 -> 40 -> 50 -> None

    print("\n🔹 Test 4: Remove from the beginning")
    sll.remove_at_start()
    sll.print_list()
    # Expected: 20 -> 25 -> 30 -> 40 -> 50 -> None

    print("\n🔹 Test 5: Remove from the end")
    sll.remove_at_end()
    sll.print_list()
    # Expected: 20 -> 25 -> 30 -> 40 -> None

    print("\n🔹 Test 6: Remove from position (index 2)")
    sll.remove_at_position(2)
    sll.print_list()
    # Expected: 20 -> 25 -> 40 -> None

    print("\n🔹 Test 7: Search for an existing element (25)")
    found, position = sll.search(25)
    print(f"Element 25 {
          'found' if found else 'not found'} at position {position}")
    # Expected: Element 25 found at position 1

    print("\n🔹 Test 8: Search for a non-existing element (100)")
    found, position = sll.search(100)
    print(f"Element 100 {
          'found' if found else 'not found'} at position {position}")
    # Expected: Element 100 not found at position -1

    print("\n🔹 Test 9: Remove from an out-of-range position (index 10)")
    sll.remove_at_position(10)
    # Expected: "Index error: out of range of the linked list."

    print("\n🔹 Test 10: Number of nodes")
    print(sll.lenght())
    # Expected: 3

    print("\n🔹 Test 11: Remove all elements until the list is empty")
    sll.remove_at_start()
    sll.remove_at_start()
    sll.remove_at_start()
    sll.print_list()
    # Expected: The linked list is empty.

    print("\n🔹 Test 12: Search in an empty list")
    found, position = sll.search(30)
    print(f"Element 30 {
          'found' if found else 'not found'} at position {position}")
    # Expected: Element 30 not found at position -1
