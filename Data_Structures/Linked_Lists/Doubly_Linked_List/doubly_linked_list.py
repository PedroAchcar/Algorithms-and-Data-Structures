class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_start(self, data):
        """Inserts a node at the beginning of the linked list."""

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

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

        while current is not None and index < position:
            previous = current
            current = current.next
            index += 1

        if current is None:
            self.insert_at_end(data)

        else:
            new_node.prev = previous
            new_node.next = current
            previous.next = new_node
            current.prev = new_node

    def insert_at_end(self, data):
        """Inserts a node at the end of the linked list."""

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_at_start(self):
        """Removes a node at the beginning of the linked list."""

        if self.head is None:
            print("The linked list is empty.")
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None

        else:
            self.head = self.head.next
            self.head.prev = None

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

        current = self.head
        index = 0

        while index < position and current is not None:
            current = current.next
            index += 1

        if current is None:  # Posição inválida
            print("Index error: out of range of the linked list.")
            return

        if current == self.tail:  # Se for o último nó, chama remove_at_end()
            self.remove_at_end()
            return

        # Atualiza os ponteiros dos nós vizinhos para remover o nó corretamente
        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev

    def remove_at_end(self):
        """Removes a node at the end of the linked list."""

        if self.head is None:
            print("The linked list is empty.")
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None

        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def print_from_head_to_tail(self):
        """Prints the linked list node by node from the head to the tail."""

        if self.head is None:
            print("The linked list is empty.")
            return

        current = self.head

        print("None <-> ", end='')

        while current:
            print(current.data, "<-> ", end='')
            current = current.next

        print("None")

    def print_from_tail_to_head(self):
        """Prints the linked list node by node from the tail to the head."""

        if self.tail is None:
            print("The linked list is empty.")
            return

        currrent = self.tail

        print("None <-> ", end='')

        while currrent:
            print(currrent.data, "<-> ", end='')
            currrent = currrent.prev

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

    dll = DoublyLinkedList()

    print("\n🔹 Test 1: Insert at the beginning")
    dll.insert_at_start(30)
    dll.insert_at_start(20)
    dll.insert_at_start(10)
    dll.print_from_head_to_tail()  # Expected: None <-> 10 <-> 20 <-> 30 <-> None

    print("\n🔹 Test 2: Insert at the end")
    dll.insert_at_end(40)
    dll.insert_at_end(50)
    # Expected: None <-> 10 <-> 20 <-> 30 <-> 40 <-> 50 <-> None
    dll.print_from_head_to_tail()

    print("\n🔹 Test 3: Insert at position (index 2)")
    dll.insert_at_position(25, 2)
    # Expected: None <-> 10 <-> 20 <-> 25 <-> 30 <-> 40 <-> 50 <-> None
    dll.print_from_head_to_tail()

    print("\n🔹 Test 4: Print in reverse order (tail -> head)")
    # Expected: None <-> 50 <-> 40 <-> 30 <-> 25 <-> 20 <-> 10 <-> None
    dll.print_from_tail_to_head()

    print("\n🔹 Test 5: Remove from the beginning")
    dll.remove_at_start()
    # Expected: None <-> 20 <-> 25 <-> 30 <-> 40 <-> 50 <-> None
    dll.print_from_head_to_tail()

    print("\n🔹 Test 6: Remove from the end")
    dll.remove_at_end()
    dll.print_from_head_to_tail()  # Expected: None <-> 20 <-> 25 <-> 30 <-> 40 <-> None

    print("\n🔹 Test 7: Remove from position (index 2)")
    dll.remove_at_position(2)
    dll.print_from_head_to_tail()  # Expected: None <-> 20 <-> 25 <-> 40 <-> None

    print("\n🔹 Test 8: Search for an existing element (25)")
    found, position = dll.search(25)
    print(f"Element 25 {
          'found' if found else 'not found'} at position {position}")
    # Expected: Element 25 found at position 1

    print("\n🔹 Test 9: Search for a non-existing element (100)")
    found, position = dll.search(100)
    print(f"Element 100 {
        'found' if found else 'not found'} at position {position}")
    # Expected: Element 100 not found at position -1

    print("\n🔹 Test 10: Remove from an out-of-range position (index 10)")
    # Expected: "Index error: out of range of the linked list."
    dll.remove_at_position(10)

    print("\n🔹 Test 11: Remove all elements until the list is empty")
    dll.remove_at_start()
    dll.remove_at_start()
    dll.remove_at_start()
    dll.print_from_head_to_tail()  # Expected: The linked list is empty.

    print("\n🔹 Test 12: Search in an empty list")
    found, position = dll.search(30)
    print(f"Element 30 {
          'found' if found else 'not found'} at position {position}")
    # Expected: Element 30 not found at position -1
