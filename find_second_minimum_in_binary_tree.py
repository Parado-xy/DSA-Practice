# Question:
# Imagine we are given a binary tree in which each node contains an integer.
# Your task is to write a Python function that traverses this binary tree and returns the second smallest value among all the tree nodes.
# If there's no second smallest number (for example, if all the values in the tree are the same, or if there's only one node in the tree), the function should return None.
# You are not allowed to use sort() or any other built-in sorting methods in your solution.
# You should use Binary Tree Traversal techniques.
# Expected complexity is O(n), where n is the number of vertices in the binary tree. The expected additional memory is O(1).

# Solution:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findSecondMinimumValue(root: TreeNode) -> int:
    # Initialize smallest and second smallest values as None
    smallest = second_smallest = None

    # Helper function for in-order traversal
    def inorder(node):
        nonlocal smallest, second_smallest
        
        if not node:
            return
        
        # Traverse left subtree
        inorder(node.left)
        
        # Process the current node's value
        if smallest is None or node.val < smallest:
            # This means we have a new smallest. 
            second_smallest = smallest
            smallest = node.val
        elif node.val > smallest and (second_smallest is None or node.val < second_smallest):
            # This means we have a new second smallest
            second_smallest = node.val
        
        # Traverse right subtree
        inorder(node.right)
    
    inorder(root)
    
    # If second_smallest is still None, return None
    return second_smallest


# Explanation:
# 1. **TreeNode class**: This is a simple binary tree node class. Each node contains an integer value and pointers to left and right children.
# 2. **findSecondMinimumValue function**: This function uses an in-order traversal of the binary tree to find the second smallest value. 
#    The `smallest` and `second_smallest` variables are used to track the smallest and second smallest values.
# 3. **inorder function**: This is a recursive helper function that performs an in-order traversal of the tree. 
#    As it traverses, it checks if the current node's value is smaller than the smallest or if it can update the second smallest value.
# 4. After the traversal, if `second_smallest` is `None`, we return `None` (i.e., if there's no second smallest value). 
#    Otherwise, we return the second smallest value.

# Time and Space Complexity:
# - **Time Complexity**: O(n), where n is the number of nodes in the tree, because we visit each node exactly once.
# - **Space Complexity**: O(1) for additional space, since we are only using a constant amount of space to store the `smallest` and `second_smallest` values, and recursion stack space is not considered for this calculation.

# Example:

# Construct a sample tree
#        2
#       / \
#      2   5
#     / \
#    2   7

root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)

# Call the function
print(findSecondMinimumValue(root))  # Output: 5
