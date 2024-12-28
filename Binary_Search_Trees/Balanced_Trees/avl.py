from print_btree import print_btree


class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


root = Node('A')
root.left = Node('B')
root.left.left = Node('C')
root.left.right = Node('D')
root.left.left.left = Node('E')
root.left.left.left.right = Node('F')
root.left.left.left.left = Node('G')
root.left.left.left.right.right = Node('H')
root.right = Node('I')

print("---------- antes ----------")
print_btree(root)


def bst_to_avl(root: Node):

    # if __name__ == "__main__":
    #     from Binary_Search_Trees.optimal_bst import main

    #     root, F, C, K = main([0, 5, 4, 7, 8, 3, 0], [6, 0, 3, 8, 7, 4, 5])
    #     print_btree(root)
