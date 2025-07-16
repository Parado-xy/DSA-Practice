class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        """
        A simple binary tree node class.
        :param value: Value of the node.
        :param left: Left child of the node.
        :param right: Right child of the node.
        """
        self.value = value
        self.left = left
        self.right = right

def is_binary_search_tree(root):
    """
    Determines if a binary tree is a binary search tree (BST).
    :param root: Root of the binary tree.
    :return: Boolean indicating whether the tree is a BST.
    """
    def validate(node, min_val, max_val):
        if not node:
            return True  # An empty subtree is a valid BST

        # Check if the current node's value is within the valid range
        if not (min_val < node.value < max_val):
            return False

        # Recursively validate the left and right subtrees
        return (validate(node.left, min_val, node.value) and
                validate(node.right, node.value, max_val))

    # Start the validation with the entire range of possible values
    return validate(root, float('-inf'), float('inf'))
