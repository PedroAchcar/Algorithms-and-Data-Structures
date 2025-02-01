import rotations as rt


class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
        self.height = 1


def update_height(node: Node) -> int:
    """Updates the node's height based on the height of its children."""

    if not node:
        return 0

    left_height = node.left.height if node.left else 0
    right_height = node.right.height if node.right else 0

    node.height = max(left_height, right_height) + 1
    return node.height


def define_rotation(node: Node) -> Node:
    """Determines and applies the appropriate rotation."""

    left_height = node.left.height if node.left else 0
    right_height = node.right.height if node.right else 0

    if left_height > right_height:
        left_left_height = node.left.left.height if node.left and node.left.left else 0
        left_right_height = node.left.right.height if node.left and node.left.right else 0

        if left_left_height > left_right_height:
            print(node.val, '-> Simple Right Rotation')
            node = rt.right_rotation(node)
        else:
            print(node.val, '-> Double Right Rotation')
            node = rt.left_right_rotation(node)

    else:
        right_right_height = node.right.right.height if node.right and node.right.right else 0
        right_left_height = node.right.left.height if node.right and node.right.left else 0

        if right_right_height > right_left_height:
            print(node.val, '-> Simple Left Rotation')
            node = rt.left_rotation(node)
        else:
            print(node.val, '-> Double Left Rotation')
            node = rt.right_left_rotation(node)

    update_height(node)
    return node


def visit_node(node: Node) -> Node:
    """Checks whether a node is balanced and applies rotation if necessary."""

    if not node:
        return None

    if node.left:
        node.left = visit_node(node.left)
    if node.right:
        node.right = visit_node(node.right)

    left_height = node.left.height if node.left else 0
    right_height = node.right.height if node.right else 0

    if abs(left_height - right_height) > 1:
        print_btree(node)
        node = define_rotation(node)
        print_btree(node)

    update_height(node)

    return node


def postorder_traversal(root: Node) -> Node:
    """Traverse the tree in post-order."""

    if not root:
        return None

    root.left = postorder_traversal(root.left)
    root.right = postorder_traversal(root.right)

    return visit_node(root)


def bst_to_avl(root: Node) -> Node:
    """Transforms a binary tree into an AVL tree."""

    return postorder_traversal(root)


if __name__ == "__main__":
    from print_btree import print_btree

    # root = Node('A')
    # root.left = Node('B')
    # root.left.left = Node('C')
    # root.left.right = Node('D')
    # root.left.left.left = Node('E')
    # root.left.left.left.right = Node('F')
    # root.left.left.left.left = Node('G')
    # root.left.left.left.right.right = Node('H')
    # root.right = Node('I')

    root = Node(4)
    root.left = Node(3)
    root.left.left = Node(1)
    root.left.left.left = Node("R0")
    root.left.left.right = Node(2)
    root.left.left.right.left = Node("R1")
    root.left.left.right.right = Node("R2")
    root.left.right = Node("R3")
    root.right = Node(5)
    root.right.left = Node("R4")
    root.right.right = Node(6)
    root.right.right.left = Node("R5")
    root.right.right.right = Node("R6")

    print("Original tree:")
    print_btree(root)

    avl_tree = bst_to_avl(root)

    print("AVL Tree:")
    print_btree(avl_tree)
