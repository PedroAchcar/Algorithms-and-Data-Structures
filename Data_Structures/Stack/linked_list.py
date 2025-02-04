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
            aux = self.head

            while aux.next:
                aux = aux.next

            aux.next = Node(data)

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


lista = LinkedList()
lista.print_list()

lista.insert_at_end(2)
lista.insert_at_end(4)
lista.insert_at_end(5)

lista.print_list()

lista.insert_at_start(1)

lista.print_list()

lista.insert_at_position(0, 0)
lista.insert_at_position(3, 2)

lista.print_list()
