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

def pre_order_traversal(root):
    if root:
        # Visit the root node (print its value)
        print(root.val, end=' ')
        
        # Recursively perform pre-order traversal of the left subtree
        pre_order_traversal(root.left)
        
        # Recursively perform pre-order traversal of the right subtree
        pre_order_traversal(root.right)

# Example usage:

# Define the adjacency list representation of the corrected BST
# Define the adjacency list representation of the BST 
adj_list = { 
    20: [10, 30], 
    10: [5, 15], 
    30: [25, 35], 
    5: [3, 7], 
    15: [12], 
    25: [23, 28], 
    35: [None, 40], 
    3: [], 
    7: [], 
    12: [],
    23: [], 
    28: [], 
    40: []
     }

# Define the root value of the BST
root_val = 20

# Build the BST from the adjacency list
root = build_tree(adj_list, root_val)

# Perform pre-order traversal and print the node values
pre_order_traversal(root) # 20 10 5 3 7 15 12 30 25 23 28 35 40
