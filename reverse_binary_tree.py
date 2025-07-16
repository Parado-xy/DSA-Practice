# Given a binary tree, write a function in Python to reverse the given binary tree. This means that for every node in the binary tree, you have to swap its left and right child nodes.

# For example, for the following binary tree

# # Original tree
# #      4
# #     / \
# #    2   5
# #   / \
# #  1   3
# the output should be

# # After reversing
# #      4
# #     / \
# #    5   2
# #       / \
# #      3   1
# The time complexity for your function should be linear, i.e., O(n), is the number of nodes in the binary tree.


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

def reverse_tree(root):
    """
    Reverses a binary tree by swapping the left and right child nodes 
    of each node in the tree using a postorder traversal.

    :param root: Root of the binary tree.
    :return: Root of the reversed binary tree.
    """
    if not root:
        return None  # If the tree is empty, nothing to reverse.

    head = root  # Keep a reference to the root of the tree for returning later.

    def postorder(node):
        """
        Performs a postorder traversal (left-right-root) to reverse the tree.
        :param node: Current node being processed.
        """
        if not node:
            return  # Base case: if the node is None, stop recursion.

        # First, traverse the right subtree
        postorder(node.right)
        # Then, traverse the left subtree
        postorder(node.left)

        # Swap left and right children
        # Redundant if-else statements handle various cases explicitly
        if node.left and node.right:
            # Case 1: Both left and right children are present
            node.left, node.right = node.right, node.left
        elif node.left and not node.right:
            # Case 2: Only left child is present
            node.left, node.right = None, node.left
        elif not node.left and node.right:
            # Case 3: Only right child is present
            node.left, node.right = node.right, None
        # Case 4 (implicitly handled): Both children are None, do nothing

    # Start the postorder traversal from the root
    postorder(root)
    
    return head  # Return the reference to the root of the reversed tree


# GPT's Code Implementation:
def reverse_tree_gpt(root):
    """
    Reverses a binary tree by swapping the left and right child nodes 
    of each node in the tree using a postorder traversal.

    :param root: Root of the binary tree.
    :return: Root of the reversed binary tree.
    """
    if not root:
        return None

    # Postorder traversal to reverse the binary tree
    def postorder(node):
        if not node:
            return
        # First reverse the left and right subtrees
        postorder(node.left)
        postorder(node.right)
        # Swap the left and right children of the current node
        node.left, node.right = node.right, node.left

    postorder(root)
    return root

            
            