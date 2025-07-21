# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int val = ...; // Value to remove
# int[] expectedNums = [...]; // The expected answer with correct length.
#                             // It is sorted with no values equaling val.

# int k = removeElement(nums, val); // Calls your implementation

# assert k == expectedNums.length;
# sort(nums, 0, k); // Sort the first k elements of nums
# for (int i = 0; i < actualLength; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

 

# Example 1:

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).
 

# Constraints:

# 0 <= nums.length <= 100
# 0 <= nums[i] <= 50
# 0 <= val <= 100
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Set some variables. 
        count = 0 
        length = len(nums)

        # Loop through the length of the array; 
        for i in range(length):
            # If the current index contains "val"
            # Set value at index i to 1000
            # Increment the count
            if nums[i] == val:
                count += 1
                nums[i] = 1000
        
        # Now sort in ascending order.
        nums.sort() 

        # Return the number of non "val" values
        return length - count
    
    def removeElement_COPILOT(self, nums: List[int], val: int) -> int:
        """
        Two-pointer approach - O(n) time, O(1) space
        """
        # 'write' pointer tracks where to place next valid element
        write = 0
        
        # 'read' pointer scans through the array
        for read in range(len(nums)):
            # If current element is not the target value
            if nums[read] != val:
                # Place it at the write position
                nums[write] = nums[read]
                write += 1
        
        return write


        