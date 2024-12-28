# Binary Search Trees (BST)

This directory contains the implementation of Binary Search Trees, a data structure that organizes elements to allow efficient search operations.

---

![Python](https://img.shields.io/badge/python-3.8-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## How OBST Works

1. Each node in the tree contains a key, a left child, and a right child.
2. Keys in the left subtree of a node are smaller than the node's key.
3. Keys in the right subtree of a node are larger than the node's key.

## Overview
An Optimal Binary Search Tree (OBST) reduces the cost of searching keys by leveraging their access probabilities. This implementation includes:
- Calculation of cost and frequency matrices.
- Construction of the OBST using dynamic programming.
- Visualization of the resulting tree structure.

## Usage Example

1. Define Input Frequencies at line 71 and 72:
f  = [0, 5, 4, 7, 8, 3, 0]
f_ = [6, 0, 3, 8, 7, 4, 5]

2. Generate OBST Matrices and Construct and Visualize the Tree running the file.

## Output

1. As output you will have the three matrices (frequency, cost and root) and the OBST:

- For the Usage Example above:

----- F Matrix -----
[[ 6. 11. 18. 33. 48. 55. 60.]
 [ 0.  0.  7. 22. 37. 44. 49.]
 [ 0.  0.  3. 18. 33. 40. 45.]
 [ 0.  0.  0.  8. 23. 30. 35.]
 [ 0.  0.  0.  0.  7. 14. 19.]
 [ 0.  0.  0.  0.  0.  4.  9.]
 [ 0.  0.  0.  0.  0.  0.  5.]]

----- C Matrix -----
[[  0.  11.  25.  58.  96. 124. 146.]
 [  0.   0.   7.  29.  66.  87. 106.]
 [  0.   0.   0.  18.  51.  72.  91.]
 [  0.   0.   0.   0.  23.  44.  63.]
 [  0.   0.   0.   0.   0.  14.  28.]
 [  0.   0.   0.   0.   0.   0.   9.]
 [  0.   0.   0.   0.   0.   0.   0.]]

----- K Matrix -----
[['-' '1' '1' '3' '3' '3' '4']
 ['0' '-' '2' '3' '4' '4' '4']
 ['0' '0' '-' '3' '4' '4' '4']
 ['0' '0' '0' '-' '4' '4' '4']
 ['0' '0' '0' '0' '-' '5' '5']
 ['0' '0' '0' '0' '0' '-' '6']
 ['0' '0' '0' '0' '0' '0' '-']]

----- Optimal Binary Search Tree -----
         ________4_______
         |              |
    _____3_____      ___5____
    |         |      |      |
 ___1____    R3     R4    __6__
 |      |                 |   |
R0    __2__              R5  R6
      |   |
     R1  R2

