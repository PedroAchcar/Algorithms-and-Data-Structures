class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

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
    linked_list = LinkedList()
    linked_list.print_list()
    linked_list.remove_at_start()
    linked_list.remove_at_position(3)
    linked_list.remove_at_end()
    print(linked_list.search(2)[0], linked_list.search(2)[1])

    linked_list.insert_at_end(2)
    linked_list.insert_at_end(4)
    linked_list.insert_at_end(5)

    linked_list.print_list()

    linked_list.insert_at_start(1)

    linked_list.print_list()

    linked_list.insert_at_position(3, 2)
    linked_list.insert_at_position(0, 0)

    linked_list.print_list()

    print(linked_list.search(0)[0], linked_list.search(0)[1])
    print(linked_list.search(3)[0], linked_list.search(3)[1])
    print(linked_list.search(7)[0], linked_list.search(7)[1])

    linked_list.remove_at_start()
    linked_list.remove_at_end()

    linked_list.print_list()

    linked_list.remove_at_position(1)

    linked_list.print_list()

    linked_list.remove_at_position(9)

    linked_list.print_list()
