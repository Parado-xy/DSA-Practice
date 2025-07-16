#!/usr/bin/env python3

class TreeNode:
    # Constructor to initialize a tree node with a given value
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def build_tree(adj_list, root_val):
    if root_val is None:
        return None

    # Create a new tree node for the root value
    root = TreeNode(root_val)

    # Get the children of the root from the adjacency list
    children = adj_list[root_val]

    # Recursively build the left and right subtrees using the children
    if children:
        root.left = build_tree(adj_list, children[0]) if len(children) > 0 else None
        root.right = build_tree(adj_list, children[1]) if len(children) > 1 else None
    return root

def in_order_traversal(root):
    if root:
        # Recursively perform in-order traversal of the left subtree
        in_order_traversal(root.left)
        
        # Visit the root node (print its value)
        print(root.val, end=' ')
        
        # Recursively perform in-order traversal of the right subtree
        in_order_traversal(root.right)

# Example usage:

# Define the adjacency list representation of the corrected BST
adj_list = {
    3: [1, 5],
    1: [0, 2],
    5: [],
    0: [],
    2: [None, 2.5],
    2.5: []
}

# Define the root value of the BST
root_val = 3

# Build the BST from the adjacency list
root = build_tree(adj_list, root_val)

# Perform in-order traversal and print the node values
in_order_traversal(root) # Output: 0 1 2 3 5

# Print a blank line.
print()
