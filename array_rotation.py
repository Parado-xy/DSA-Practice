# Let me explain array/matrix rotation with clear examples.



# For Arrays (1D rotation):
# Array rotation means moving elements by a certain number of positions, either left or right. 
# Elements that "fall off" one end wrap around to the other end.

# 1. Left Rotation:
# ```python
# # Original array:     [1, 2, 3, 4, 5]
# # Left rotate by 2:   [3, 4, 5, 1, 2]

# def left_rotate(arr, k):
#     k = k % len(arr)  # Handle cases where k > len(arr)
#     return arr[k:] + arr[:k]
# ```

# 2. Right Rotation:
# ```python
# # Original array:     [1, 2, 3, 4, 5]
# # Right rotate by 2:  [4, 5, 1, 2, 3]

# def right_rotate(arr, k):
#     k = k % len(arr)  # Handle cases where k > len(arr)
#     return arr[-k:] + arr[:-k]
# ```

# For Matrices (2D rotation):
# Matrix rotation typically means rotating the entire matrix by 90, 180, or 270 degrees clockwise or counterclockwise. 
# Here's a visual example of 90-degree clockwise rotation:

# Original Matrix:
# ```
# 1  2  3
# 4  5  6
# 7  8  9
# ```

# 90° Clockwise:
# ```
# 7  4  1
# 8  5  2
# 9  6  3
# ```

# Here's a Python implementation for 90-degree clockwise rotation:

# ```python
# def rotate_matrix_90_clockwise(matrix):
#     n = len(matrix)
#     # Create new matrix with same dimensions
#     result = [[0 for _ in range(n)] for _ in range(n)]
    
#     # Fill the result matrix
#     for i in range(n):
#         for j in range(n):
#             result[j][n-1-i] = matrix[i][j]
    
#     return result
# ```

# Key things to note:
# 1. For arrays:
#    - Rotation preserves the order of elements
#    - Elements wrap around
#    - Time complexity can be O(n) for a single rotation
#    - Space complexity can be O(1) with in-place rotation techniques

# 2. For matrices:
#    - Each element's new position can be calculated mathematically
#    - For a clockwise 90° rotation:
#      - row becomes column: j = new_row
#      - column becomes n-1-row: n-1-i = new_col
#    - Can be done in-place for square matrices
#    - Time complexity is O(n²) where n is the matrix dimension

# In linear algebra, the transpose of a matrix is an operator which flips a matrix over its diagonal; 
# that is, it switches the row and column indices of the matrix A by producing another matrix, often denoted by A^T

# Here's an in-place matrix rotation algorithm that's more space-efficient:

# ```python
# def rotate_matrix_in_place(matrix):
#     n = len(matrix)
    
#     # First, transpose the matrix
#     for i in range(n):
#         for j in range(i, n):
#             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
#     # Then reverse each row
#     for i in range(n):
#         matrix[i].reverse()
    
#     return matrix
# ```

# You are provided with an array of n integers and a number k. 
# Your task is to perform an anti-clockwise rotation (toward the front) of the array by k positions. 
# The rotation should be done in place, which means you have to directly manipulate the input array without creating a new one. 
# Note that k might be bigger than the array length.

# For example, if the input array is [1, 2, 3, 4, 5, 6, 7], and k = 3, then after the operation, the input array should look like [4, 5, 6, 7, 1, 2, 3].

# My solution. It works, but it technically doesn't meet the inplace requirement because i used slicing:
# EDIT: This was actually correct, they just didn't wnat me to return anything. 
# Yet, here i was trying to figure out how to rotate an array through some sort of for loop.
from typing import List
def anti_rotate_array(nums: List[int], k: int) -> None:
    if len(nums) == 0: 
        return 
    k = abs(k)
    k %= len(nums) # Keep k in range of the array.
    nums[k:] , nums[:k] =  nums[:k], nums[k:] 

# Test case where k is larger than the list length
nums = [1, 2, 3, 4, 5]
k = 7  # Equivalent to rotating left by k = 2 (since 7 % 5 = 2)
anti_rotate_array(nums, k)
print(nums)  # Expected output: [3, 4, 5, 1, 2]

# Edge case where k is 0 (no rotation)
nums = [1, 2, 3, 4, 5]
k = 0  # Expect no change
anti_rotate_array(nums, k)
print(nums)  # Expected output: [1, 2, 3, 4, 5]

# Negative k (if function is modified to handle negative shifts)
nums = [1, 2, 3, 4, 5]
k = -2  # Would expect a leftward rotation by 2
anti_rotate_array(nums, k)
print(nums) # Expected output: [3, 4, 5, 1, 2]

# Empty list
nums = []
k = 3  # Any rotation should just return []
anti_rotate_array(nums, k)
print(nums)  # Expected output: []

# Single-element list
nums = [42]
k = 1000  # Large k should still return [42]
anti_rotate_array(nums, k)
print(nums)  # Expected output: [42]




# Here's everything given back by GPT:
# from typing import List

# def anti_rotate_array(nums: List[int], k: int) -> None:
#     """
#     Rotate the list to the left by `k` positions.
#     This rotation modifies the array in-place and does not return anything.
#     """
#     # Modulo k to handle cases where k > len(nums)
#     k %= len(nums)
    
#     # Perform the left rotation by slicing and rearranging the array
#     nums[:] = nums[k:] + nums[:k]  # Left rotation by `k`
    
# # Example usage:
# nums = [1, 3, 5, 6, 8, 2, 4, 9]
# anti_rotate_array(nums, 5)
# print(nums)


# Question:
# You are given a list of integers, nums, and an integer k. 
# Your task is to rotate the list to the left by k positions if k is positive. 
# If k is negative, rotate the list to the right by |k| positions.
# Additionally, the function should handle the following cases:
# - If the list is empty, return it as is.
# - If k is larger than the list's length, keep k within the bounds of the list length by using k % len(nums).
# - Your function should modify the list in-place.

# Example:
# anti_rotate_array([1, 2, 3, 4, 5], -2) should yield [4, 5, 1, 2, 3]
# anti_rotate_array([], 3) should yield []
# anti_rotate_array([42], 1000) should yield [42]

from typing import List

def anti_rotate_array_gpt(nums: List[int], k: int) -> None:
    # Check for empty list, which requires no rotation
    if not nums:
        return
    
    # Adjust k to always fall within the array bounds by using absolute k modulo the list length
    k = abs(k) % len(nums)
    
    # If k is zero after modulo adjustment, no rotation is needed, so we exit early
    if k == 0:
        return
    
    # Perform left rotation by k for positive k and right rotation by k for negative k
    # The list slices are swapped to move elements accordingly
    nums[k:], nums[:k] = nums[:k], nums[k:]

class Solution:
    # Rotate to the right. 
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        # Take the last `k` elements to the front, and the first len(nums) - k elements 
        # To the back. 
        nums[:] = nums[-k:] + nums[:-k]
        

# Testing the function with various cases
print(anti_rotate_array_gpt([1, 2, 3, 4, 5], -2))  # Expected rightward rotation result: [4, 5, 1, 2, 3]
print(anti_rotate_array_gpt([], 3))                # Expected empty list result: []
print(anti_rotate_array_gpt([42], 1000))           # Expected single element result: [42]
nums = [i for i in range(1, 100001)]  # A large array with 100,000 elements
k = 99999  # A large positive k value close to the length of the array
with open('numbers.txt','w') as file:
    anti_rotate_array(nums, k)
    print(nums, file = file)
# Knowing how to code is ELITE