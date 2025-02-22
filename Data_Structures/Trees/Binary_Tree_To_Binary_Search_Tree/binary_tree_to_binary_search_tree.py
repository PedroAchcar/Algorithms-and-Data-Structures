class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def __inorder_traversal(self, node: Node, array: list):
        """Stores the inorder traversal of the tree in array."""

        if node is None:
            return

        self.__inorder_traversal(node.left, array)

        array.append(node.val)

        self.__inorder_traversal(node.right, array)

    def __array_to_bst(self, node: Node, sorted_values: list, index: int) -> int:
        """Converts the tree to a BST using other inorder traversal."""

        if node is None:
            return index

        index = self.__array_to_bst(node.left, sorted_values, index)

        node.val = sorted_values[index]
        index += 1

        index = self.__array_to_bst(node.right, sorted_values, index)
        return index

    def convert_to_bst(self):
        """Converts the binary tree to a BST without changing its structure."""

        values = []
        self.__inorder_traversal(self.root, values)

        values.sort()

        self.__array_to_bst(self.root, values, 0)


if __name__ == "__main__":

    from print_btree import print_btree

    bt = BinaryTree()
    bt.root = Node(10)
    bt.root.left = Node(2)
    bt.root.right = Node(7)
    bt.root.left.left = Node(8)
    bt.root.left.right = Node(4)
    bt.root.right.left = Node(5)
    bt.root.right.right = Node(3)

    print("Original Binary Tree:")
    print_btree(bt.root)

    bt.convert_to_bst()

    print("Binary Search Tree with the same structure of the original Binary Tree:")
    print_btree(bt.root)
