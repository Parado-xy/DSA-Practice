# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109

from typing import List

def move_left(nums: List[int], current_index: int )-> int:

    prev_val = nums[current_index]
    prev_index = current_index
    current = nums[current_index]

    while True:
        if(prev_val == current):
            prev_index -= 1
            # Check if we indexed out of range; 
            if not (prev_index < 0) and not (prev_index > len(nums) -1):
                prev_val = nums[prev_index]
            else:
                return prev_index + 1    
        else:
            return prev_index + 1
            
def move_right(nums: List[int], current_index: int )-> int:

    next_val = nums[current_index]
    next_index = current_index
    current = nums[current_index]

    while True:
        if(next_val == current):
            next_index += 1
            # Check if we indexed out of range; 
            if not (next_index < 0) and not (next_index > len(nums) -1):
                next_val = nums[next_index]
            else:
                return next_index - 1
        else:
            return next_index - 1

    


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        This method finds the target via binary search, then expands linearly. 
        """

        # If the target is not in nums, return early
        if (target not in nums):
            return [-1, -1]

        L, R = 0, len(nums) - 1

        while (L <= R):
            mid = L + (R - L) // 2

            if(nums[mid] == target):
                return [move_left(nums, mid), move_right(nums, mid)]

            elif (nums[mid] > target):
                R = mid - 1
            else:
                L = mid + 1

        # This is redundant because of the first check. 
        # I'm adding it to satisfy the type checking. 
        return [-1, -1]
    

# Here lies copilot's solution. 
class SolutionCopilot:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Find first and last position using two binary searches.
        Time: O(log n), Space: O(1)
        """
        if not nums:
            return [-1, -1]
        
        def find_first_position(nums, target):
            """Binary search for leftmost occurrence"""
            left, right = 0, len(nums) - 1
            result = -1
            
            while left <= right:
                mid = left + (right - left) // 2
                
                if nums[mid] == target:
                    result = mid  # Found target, but keep searching left
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return result
        
        def find_last_position(nums, target):
            """Binary search for rightmost occurrence"""
            left, right = 0, len(nums) - 1
            result = -1
            
            while left <= right:
                mid = left + (right - left) // 2
                
                if nums[mid] == target:
                    result = mid  # Found target, but keep searching right
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return result
        
        first = find_first_position(nums, target)
        if first == -1:  # Target not found
            return [-1, -1]
        
        last = find_last_position(nums, target)
        return [first, last]

        
        
        