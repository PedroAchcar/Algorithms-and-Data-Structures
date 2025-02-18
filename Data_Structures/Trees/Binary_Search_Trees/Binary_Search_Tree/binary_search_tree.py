class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value, node=None):
        """Inserts a node into a binary tree."""

        if node is None:
            node = self.root

        if self.root is None:
            self.root = Node(value)
            return self.root

        if value < node.val:
            if node.left is None:
                node.left = Node(value)

            else:
                self.insert(value, node.left)

        elif value > node.val:
            if node.right is None:
                node.right = Node(value)

            else:
                self.insert(value, node.right)

        return self.root

    def search(self, value, node=None):
        """Searches for a node in a binary tree."""

        if node is None:
            node = self.root

        if self.root is None:
            return False

        if value == node.val:
            return True

        if value < node.val and node.left is not None:
            return self.search(value, node.left)

        if value > node.val and node.right is not None:
            return self.search(value, node.right)

        return False

    def remove(self, value, node=None, parent=None):
        """Removes a node from a binary tree."""

        if node is None:
            node = self.root

        if self.root is None:
            return False

        if value < node.val:
            if node.left:
                return self.remove(value, node.left, node)

            else:
                return False

        elif value > node.val:
            if node.right:
                return self.remove(value, node.right, node)

            else:
                return False

        else:
            if node.left is None and node.right is None:
                if parent:
                    if parent.left == node:
                        parent.left = None

                    else:
                        parent.right = None

                else:
                    self.root = None

                return True

            elif node.left is None:
                if parent:
                    if parent.left == node:
                        parent.left = node.right

                    else:
                        parent.right = node.right

                else:
                    self.root = node.right

                return True

            elif node.right is None:
                if parent:
                    if parent.left == node:
                        parent.left = node.left

                    else:
                        parent.right = node.left

                else:
                    self.root = node.left

                return True

            else:
                successor = self.find_maximum(node.left)
                node.val = successor.val
                return self.remove(successor.val, node.left, node)

    def find_minimum(self, node=None):
        """Finds the minimum node of a binary tree."""

        if node is None:
            node = self.root

        if self.root is None:
            return None

        current = node

        while current.left is not None:
            current = current.left

        return current

    def find_maximum(self, node=None):
        """Finds the maximum node of a binary tree."""

        if node is None:
            node = self.root

        if self.root is None:
            return None

        current = node

        while current.right is not None:
            current = current.right

        return current

    def preorder_traversal(self, node=None):
        """Traverses the tree in preorder traversal."""

        if node is None:
            node = self.root

        if node is None:
            print("The tree is empty.")
            return

        print(node.val, end=" ")

        if node.left:
            self.preorder_traversal(node.left)

        if node.right:
            self.preorder_traversal(node.right)

    def inorder_traversal(self, node=None):
        """Traverses the tree in inorder traversal."""

        if node is None:
            node = self.root

        if node is None:
            print("The tree is empty.")
            return

        if node.left:
            self.inorder_traversal(node.left)

        print(node.val, end=" ")

        if node.right:
            self.inorder_traversal(node.right)

    def postorder_traversal(self, node=None):
        """Traverses the tree in postorder traversal."""

        if node is None:
            node = self.root

        if node is None:
            print("The tree is empty.")
            return

        if node.left:
            self.postorder_traversal(node.left)

        if node.right:
            self.postorder_traversal(node.right)

        print(node.val, end=" ")


if __name__ == "__main__":

    from print_btree import print_btree

    bst = BinarySearchTree()

    print("\n🔹 Test 1: Insert elements into the BST with in-order traversal:")
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    print_btree(bst.root)

    bst.inorder_traversal()
    # Expected: 20 30 40 50 60 70 80

    print("\n\n🔹 Test 2: Search for elements:")
    print(f"Searching for 40: {bst.search(40)}")
    # Expected: Searching for 40: True
    print(f"Searching for 100: {bst.search(100)}")
    # Expected: Searching for 100: False

    print("\n🔹 Test 3: Find the minimum value in the BST:")
    min_node = bst.find_minimum()
    print(f"Minimum value: {min_node.val}")
    # Expected: Minimum value: 20

    print("\n🔹 Test 4: Find the maximum value in the BST:")
    max_node = bst.find_maximum()
    print(f"Maximum value: {max_node.val}")
    # Expected: Maximum value: 80

    print("\n🔹 Test 5: Remove a leaf node (20):")
    bst.remove(20)
    print_btree(bst.root)
    bst.inorder_traversal()
    # Expected: 30 40 50 60 70 80

    print("\n\n🔹 Test 6: Remove a node with one child (30):")
    bst.remove(30)
    print_btree(bst.root)
    bst.inorder_traversal()
    # Expected: 40 50 60 70 80

    print("\n\n🔹 Test 7: Remove a node with two children (50):")
    bst.remove(50)
    print_btree(bst.root)
    bst.inorder_traversal()
    # Expected: 40 60 70 80

    print("\n\n🔹 Test 8: Traversals:")
    print("Preorder traversal:")
    bst.preorder_traversal()
    # Expected: 60 40 70 80

    print("\nInorder traversal:")
    bst.inorder_traversal()
    # Expected: 40 60 70 80

    print("\nPostorder traversal:")
    bst.postorder_traversal()
    # Expected: 40 80 70 60

    print("\n\n🔹 Test 9: Remove all nodes and check if the tree is empty:")
    bst.remove(40)
    bst.remove(60)
    bst.remove(70)
    bst.remove(80)
    bst.inorder_traversal()
    # Expected: The tree is empty.
    print("Is tree empty?", bst.root is None)
    # Expected: Is tree empty? True
