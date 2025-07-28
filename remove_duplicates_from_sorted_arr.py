# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

 

# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.

from typing import List

class Solution:
    def removeDuplicates_NAIVE(self, nums: List[int]) -> int:
        
        # Get infinity. 
        inf = float("inf")

        # Get previous and current pointers. 
        prev = curr = 0

        # get the length of the list.
        length = len(nums)

        # Keep a count of removed values.
        count = 0 

        for i in range(length):
            curr += 1

            if(curr == length):
                break 

            if (nums[prev] == nums[curr]):
                # If the current value is equal to the previous value,
                nums[curr] = inf # Remove this occurrence.
                count += 1 
            else: 
                # We only move the prev pointer when prev != current 
                prev = curr 

        # sort the list. 
        nums.sort()        

        return length - count

    # This uses the two-pointer approach.     
    def removeDuplicates(self, nums):
        if not nums:  # Handle empty list case
            return 0

        j = 0  # Pointer for the position of unique elements
        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                j += 1  # Move to the next position for unique element
                nums[j] = nums[i]  # Assign the unique element

        return j + 1  # Return the length of the list with unique elements

                



