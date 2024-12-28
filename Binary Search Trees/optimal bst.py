import numpy as np

from print_btree import print_btree


def minimal_cost(C, i, j):
    min_cost = float('inf')
    K = 0
    for k in range(i + 1, j + 1):
        cost = C[i][k - 1] + C[k][j]
        if cost < min_cost:
            min_cost = cost
            K = k
    return min_cost, K


def optimal_tree(f, f_):
    n = len(f) - 1
    C = np.zeros([n+1, n+1])
    F = np.zeros([n+1, n+1])
    # It needs to be a list of lists because numpy doesn't accept placing str in an array of zeros
    K = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for j in range(n + 1):
        C[j][j] = 0
        F[j][j] = f_[j]

    for d in range(1, n + 1):
        for i in range(n - d + 1):
            j = i + d
            F[i][j] = F[i][j - 1] + f[j] + f_[j]
            min_cost, K[i][j] = minimal_cost(C, i, j)
            C[i][j] = min_cost + F[i][j]

    # Place "-" on the main diagonal to make it easier to visualize, it isn't necessary
    for k in range(n + 1):
        K[k][k] = '-'

    return F, C, K


class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def build_tree(K, i, j):
    if i > j:
        return None
    if i == j:
        return Node(f'R{i}')
    root_index = K[i][j]
    root = Node(f'{root_index}')
    root.left = build_tree(K, i, root_index - 1)
    root.right = build_tree(K, root_index, j)
    return root


# It works, but I found a better lib
# def print_tree(root, level=0, prefix="\nRaiz: "):
#     if root is not None:
#         print(" " * (level * 4) + prefix + str(root.val))
#         print_tree(root.left, level + 1, "L--- ")
#         print_tree(root.right, level + 1, "R--- ")


# Usage exemple
f = [0, 10, 20, 30, 40, 50, 60, 70, 80]
f_ = [10, 10, 10, 10, 10, 10, 10, 10, 10]


F, C, K = optimal_tree(f, f_)
print('----- F Matrix -----')
print(F)
print('\n----- C Matrix -----')
print(C)
print('\n----- K Matrix -----')
print(np.matrix(K))  # Transform to np.array to print with numpy formatting


# Build the tree
root = build_tree(K, 0, len(K) - 1)


# Print the tree
# print_tree(root)
print('\n----- Optimal Binary Search Tree -----')
print_btree(root)
