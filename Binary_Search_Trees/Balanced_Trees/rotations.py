def right_rotation(p):
    u = p.right
    p.right = u.left
    u.left = p
    return u


def left_right_rotation(p):
    u = p.left
    v = u.right
    u.right = v.left
    p.left = v.right
    v.left = u
    v.right = p
    return v


def left_rotation(p):
    u = p.right
    p.right = u.left
    u.left = p
    return u


def right_left_rotation(p):
    u = p.right
    v = u.left
    u.left = v.right
    p.right = v.left
    v.right = u
    v.left = p
    return v


if __name__ == "__main__":
    from print_btree import print_btree

    class Node:
        def __init__(self, data):
            self.val = data
            self.left = None
            self.right = None

    print("---------- Simple Right Rotation ----------")
    root = Node("p")
    root.left = Node("T1")
    root.right = Node("u")
    root.right.left = Node("T2")
    root.right.right = Node("T3")

    print_btree(root)
    balanced = right_rotation(root)
    print_btree(balanced)

    print("---------- Double Right Rotation ----------")
    root = Node("p")
    root.left = Node("u")
    root.right = Node("T4")
    root.left.left = Node("T1")
    root.left.right = Node("v")
    root.left.right.left = Node('T2')
    root.left.right.right = Node('T3')

    print_btree(root)
    balanced = left_right_rotation(root)
    print_btree(balanced)

    print("---------- Simple Left Rotation ----------")
    root = Node("p")
    root.left = Node("T1")
    root.right = Node("u")
    root.right.left = Node("T2")
    root.right.right = Node("T3")

    print_btree(root)
    balanced = left_rotation(root)
    print_btree(balanced)

    print("---------- Double Left Rotation ----------")
    root = Node("p")
    root.left = Node("T1")
    root.right = Node("u")
    root.right.left = Node("v")
    root.right.right = Node("T4")
    root.right.left.left = Node('T2')
    root.right.left.right = Node('T3')

    print_btree(root)
    balanced = right_left_rotation(root)
    print_btree(balanced)
