# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

 

# Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Get the length of each row
        n = len(matrix[0])
        for row in matrix:
            for i in range(n - 1, -1, -1):
                if row[i] < target: 
                    break 
                elif row[i] == target: 
                    return True

        return False
    
# The approach to this is logically simple. 
# We can start searching from the last element of each row. 
# If the last element is less than the target, then we know that our target can't be in that row. 
# We move to the next row. If the last element of this row is less than the target, we move left
# We return the target when we find it.  
        