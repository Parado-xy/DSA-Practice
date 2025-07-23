# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
 

# Constraints:

# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        L, R = 0, len(nums) 

        while (L <= R): 

            mid = L + (R - L) // 2 # This formula add the difference between ( L & R ) // 2 to L

            # If the current middle element is the target, return it. 
            if(nums[mid] == target):
                return mid
            elif (nums[mid] > target):
                # If the current middle is greater than the target, cut out the right half; 
                R = mid - 1
            else: 
                # If we get here, means the current mid is less than the target
                # Here, we cut off the Left half; 
                L = mid + 1  


        # If we haven't found it at this point, it means it does not exist in the array.
        return -1    


# Here's a stellar blog post. 
# https://leetcode.com/discuss/study-guide/2371234/An-opinionated-guide-to-binary-search-(comprehensive-resource-with-a-bulletproof-template)/1532153#template       
        