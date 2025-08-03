# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:

# Input: root = [1,null,2]
# Output: 2
 

# Constraints:
# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # If no root node, then we have a deoth of zero. 
        if not root:
            return 0

        max_depth = current_depth = 1

        # Helper Function for in-order traversal
        def inorder(node):
            nonlocal max_depth, current_depth

            if not node:
                # If this node we entered is invalid 
                # We return and move up a depth
                current_depth -= 1
                return 

            # Let's increment the current debth anytime we go a step down
            current_depth += 1
            inorder(node.left) 

            # After any change in current_depth, we check if it's greater than the max_depth
            if current_depth > max_depth:
                max_depth = current_depth

            # Let's increment the current debth anytime we go a step down
            current_depth += 1
            inorder(node.right)

            # After any change in current_depth, we check if it's greater than the max_depth
            if current_depth > max_depth:
                max_depth = current_depth

            # If we've traversed both nodes, we're going back up so decrement current depth
            current_depth -= 1

        # Traverse the tree. 
        inorder(root)

        return max_depth

    # It turns out that my solution was overally complex. Crazy. 
    def maxDepth_COPILOT(self, root: Optional[TreeNode]) -> int:
        """
        Simple recursive approach
        Time: O(n), Space: O(h) where h is height
        """
        # Base case: empty tree has depth 0
        if not root:
            return 0
        
        # Recursive case: 1 + max depth of subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        return 1 + max(left_depth, right_depth)


        