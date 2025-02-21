class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.children = []


def general_tree_to_binary_tree(root: Node) -> Node:
    """Converts a general tree to a binary tree."""

    if not root:
        return None

    binary_node = Node(root.val)

    if root.children:
        binary_node.left = general_tree_to_binary_tree(root.children[0])

    current = binary_node.left

    for child in root.children[1:]:
        current.right = general_tree_to_binary_tree(child)
        current = current.right

    return binary_node


if __name__ == "__main__":

    from print_btree import print_btree

    root = Node('A')
    root.children.append(Node('B'))
    root.children.append(Node('C'))
    root.children.append(Node('D'))

    root.children[0].children.append(Node('E'))

    root.children[1].children.append(Node('F'))
    root.children[1].children.append(Node('G'))
    root.children[1].children.append(Node('H'))

    root.children[2].children.append(Node('I'))
    root.children[2].children.append(Node('J'))

    root.children[2].children[1].children.append(Node('K'))

    print("\n\nGeneral Tree:")
    print("           A             ")
    print("        /  |  \\         ")
    print("      /    |    \\       ")
    print("    B      C      D      ")
    print("  /      / | \\   / \\   ")
    print(" E      F  G  H I   J    ")
    print("                   /     ")
    print("                  K      ")

    binaryTreeRoot = general_tree_to_binary_tree(root)

    print("Binary Tree:")
    print_btree(binaryTreeRoot)
