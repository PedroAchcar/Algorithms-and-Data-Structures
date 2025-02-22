# Binary Tree to a Binary Search Tree Implementation

This repository contains an implementation of a convertion of a binary tree to a BST using an inorder traversal.


## Class Structure
### `Node`
Represents a node.
```python
class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
```

### `BinaryTree`
Manages the convertion.
```python
class BinaryTree:
    def __init__(self):
        self.root = None
```

### Methods
#### Convertion Operations
- `convert_to_bst()`: Converts the binary tree to a BST without changing its structure.

## Usage and Test Cases
To use this stack implementation, create an instance of a `BinaryTree` and call the available method as needed.

```python
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
```

## Expected Output
```
Original Binary Tree:
 ____10____
 |        |
_2_      _7_
| |      | |
8 4      5 3


Binary Search Tree with the same structure of the original Binary Tree:
 ____5____
 |       |
_3_    __8__
| |    |   |
2 4    7  10
```
