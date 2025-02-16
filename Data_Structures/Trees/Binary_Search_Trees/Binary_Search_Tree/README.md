# Binary Search Tree Implementation

This repository contains an implementation of a **Binary Search Tree (BST)** in Python. The `BinarySearchTree` class provides methods for insertion, search, deletion, and tree traversal operations.

## Features
- Insert elements into the BST.
- Search for a specific element in the tree.
- Remove elements, including cases with no children, one child, or two children.
- Find the minimum and maximum values in the BST.
- Perform **preorder, inorder, and postorder traversals** of the BST.

## Class Structure

### `Node`
Represents a node in the BST.
```python
class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
```

### `BinarySearchTree`
Manages the BST operations.
```python
class BinarySearchTree:
    def __init__(self):
        self.root = None
```

### Methods
#### Tree Operations
- `insert(value)`: Inserts a value into the BST.
- `search(value)`: Searches for a value in the BST.
- `remove(value)`: Removes a value from the BST.
- `find_minimum()`: Finds the node with the minimum value.
- `find_maximum()`: Finds the node with the maximum value.
- `preorder_traversal()`: Performs a preorder traversal.
- `inorder_traversal()`: Performs an inorder traversal.
- `postorder_traversal()`: Performs a postorder traversal.

## Usage and Test Cases
To use this BST implementation, create an instance of `BinarySearchTree` and call the available methods as needed.

```python
if __name__ == "__main__":

    bst = BinarySearchTree()

    print("\n🔹 Test 1: Insert elements into the BST with in-order traversal:")
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

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
    bst.inorder_traversal()
    # Expected: 30 40 50 60 70 80

    print("\n\n🔹 Test 6: Remove a node with one child (30):")
    bst.remove(30)
    bst.inorder_traversal()
    # Expected: 40 50 60 70 80

    print("\n\n🔹 Test 7: Remove a node with two children (50):")
    bst.remove(50)
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
```

## Expected Output
```
🔹 Test 1: Insert elements into the BST with in-order traversal:
     ______50_______   
     |             |   
 ___30___      ___70___
 |      |      |      |
20     40     60     80


20 30 40 50 60 70 80   

🔹 Test 2: Search for elements:
Searching for 40: True
Searching for 100: False

🔹 Test 3: Find the minimum value in the BST:
Minimum value: 20

🔹 Test 4: Find the maximum value in the BST:
Maximum value: 80

🔹 Test 5: Remove a leaf node (20):
 _____50______
 |           |
30__     ___70___
   |     |      |
  40    60     80


30 40 50 60 70 80

🔹 Test 6: Remove a node with one child (30):
 ___50_____
 |        |
40    ___70___
      |      |
     60     80


40 50 60 70 80 

🔹 Test 7: Remove a node with two children (50):
40____
     |
 ___70___
 |      |
60     80


40 60 70 80

🔹 Test 8: Traversals:
Preorder traversal:
40 70 60 80
Inorder traversal:
40 60 70 80
Postorder traversal:
60 80 70 40

🔹 Test 9: Remove all nodes and check if the tree is empty:
The tree is empty.
Is tree empty? True
```
