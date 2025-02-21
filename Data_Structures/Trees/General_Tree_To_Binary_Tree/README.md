# General Tree to Binary Tree Conversion

This repository contains an implementation of a **General Tree to Binary Tree conversion** using the **child-sibling representation**. The `general_tree_to_binary_tree` function converts a general tree into a binary tree where the first child becomes the left child and the subsequent siblings are linked as right children.

## Features
- Convert a general tree to a binary tree.
- Maintain the structure of a general tree using left-child right-sibling representation.
- Visualize both general and binary trees.

## Class Structure
### `Node`
Represents a node in both the general tree and the binary tree.
```python
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.children = []  # List of children (only for general tree)
```

## Conversion Function
### `general_tree_to_binary_tree`
Converts a general tree to a binary tree using left-child right-sibling representation.
```python
def general_tree_to_binary_tree(root: Node) -> Node:
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
```

## Usage and Test Cases
To use this implementation, define a general tree and convert it to a binary tree.

```python
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
```

## Expected Tree Structure
### General Tree:
```
           A
        /  |  \          
      /    |    \        
    B      C      D      
  /      / | \   / \     
 E      F  G  H I   J    
                   /     
                  K
```

### Converted Binary Tree:
```
   _____A
   |
___B_____
|       |
E   ____C____
    |       |
    F_    __D
     |    |
     G_   I_
      |    |
      H   _J
          |
          K
```

This representation follows the **left-child right-sibling** model where:
- The first child of a node is stored as its left child.
- The subsequent siblings are stored as right children.

## Notes
- Ensure that `print_btree` is available to visualize the binary tree properly.
