# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
 

# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105
# 

from typing import List 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Initialize result list
        answer = []
        
        # Handle edge cases
        if len(nums) < 3:
            return answer
            
        # Sort the array to handle duplicates and enable two-pointer technique
        nums.sort()
        
        # Iterate through each possible first element
        for i in range(len(nums) - 2):
            # Skip duplicates for i to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Use two pointers: j starts after i, k starts at the end
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]
                
                if curr_sum == 0:
                    # Found a valid triplet
                    answer.append([nums[i], nums[j], nums[k]])
                    # Skip duplicates for j and k
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif curr_sum < 0:
                    # Sum is too small, increment j to increase sum
                    j += 1
                else:
                    # Sum is too large, decrement k to decrease sum
                    k -= 1
        
        return answer
    

# Let’s dive into the two-pointer technique used in the corrected 3Sum solution, focusing on how it works within the `while j < k` loop to find triplets that sum to zero. I’ll explain the logic step-by-step, keeping it clear and concise, as you’re specifically asking about this part.

# ### Context
# In the 3Sum problem, we need to find all unique triplets `[nums[i], nums[j], nums[k]]` in a sorted array `nums` such that `nums[i] + nums[j] + nums[k] == 0`, with `i < j < k`. The array is sorted upfront to make it easier to handle duplicates and use the two-pointer technique efficiently.

# The outer loop iterates over index `i`, fixing the first element `nums[i]`. For each `i`, we need to find a pair of indices `j` and `k` (where `i < j < k`) such that `nums[j] + nums[k] = -nums[i]`. This reduces the problem to a "two-sum" problem for the subarray after `i`. The two-pointer technique solves this two-sum problem.

# ### Two-Pointer Technique in the Code
# Here’s the relevant part of the code:

# ```python
# j = i + 1
# k = len(nums) - 1
# while j < k:
#     curr_sum = nums[i] + nums[j] + nums[k]
#     if curr_sum == 0:
#         answer.append([nums[i], nums[j], nums[k]])
#         while j < k and nums[j] == nums[j + 1]:
#             j += 1
#         while j < k and nums[k] == nums[k - 1]:
#             k -= 1
#         j += 1
#         k -= 1
#     elif curr_sum < 0:
#         j += 1
#     else:
#         k -= 1
# ```

# Let’s break down how the two pointers (`j` and `k`) work:

# 1. **Initialization**:
#    - `j = i + 1`: The left pointer `j` starts just after `i` to ensure `j > i`.
#    - `k = len(nums) - 1`: The right pointer `k` starts at the end of the array to ensure `k > j`.
#    - This setup guarantees `i < j < k`, which is required for valid triplets.

# 2. **Loop Condition (`while j < k`)**:
#    - The loop continues as long as `j < k`, meaning the pointers haven’t crossed. If `j >= k`, we can’t form a triplet with `j < k`, so we stop.

# 3. **Calculating the Sum**:
#    - Compute `curr_sum = nums[i] + nums[j] + nums[k]`.
#    - Since we want `curr_sum == 0`, this is equivalent to finding `nums[j] + nums[k] = -nums[i]`.

# 4. **Three Cases Based on `curr_sum`**:
#    - **Case 1: `curr_sum == 0`**:
#      - We’ve found a valid triplet `[nums[i], nums[j], nums[k]]` that sums to zero.
#      - Append it to the result: `answer.append([nums[i], nums[j], nums[k]])`.
#      - To avoid duplicate triplets, skip over duplicate values of `nums[j]` and `nums[k]`:
#        - `while j < k and nums[j] == nums[j + 1]: j += 1` skips all consecutive duplicates of `nums[j]`.
#        - `while j < k and nums[k] == nums[k - 1]: k -= 1` skips all consecutive duplicates of `nums[k]`.
#      - Move both pointers inward: `j += 1` and `k -= 1` to look for the next potential pair.
#    - **Case 2: `curr_sum < 0`**:
#      - The sum is too small (negative). Since the array is sorted (`nums[j] <= nums[j+1]`), increasing `j` to a larger value might increase the sum toward zero.
#      - Increment `j`: `j += 1`.
#    - **Case 3: `curr_sum > 0`**:
#      - The sum is too large (positive). Since the array is sorted (`nums[k] >= nums[k-1]`), decreasing `k` to a smaller value might decrease the sum toward zero.
#      - Decrement `k`: `k -= 1`.

# 5. **Why It Works**:
#    - **Sorted Array**: Sorting ensures that moving `j` right increases the sum (larger `nums[j]`), and moving `k` left decreases the sum (smaller `nums[k]`). This allows us to systematically adjust the sum toward zero.
#    - **Efficiency**: For each `i`, the `j` and `k` pointers traverse the subarray at most once (since `j` only increases and `k` only decreases), making the inner loop O(n).
#    - **Duplicate Handling**: Skipping duplicates ensures we only include unique triplets. For example, if `nums[j] == nums[j+1]`, we skip to avoid reusing the same `nums[j]` value in another triplet.

# ### Example Walkthrough
# Let’s trace with `nums = [-1, 0, 1, 2, -1, -4]` after sorting: `[-4, -1, -1, 0, 1, 2]`, for `i = 1` (`nums[i] = -1`).

# - Target: `nums[j] + nums[k] = -nums[i] = -(-1) = 1`.
# - Initialize: `j = 2` (`nums[j] = -1`), `k = 5` (`nums[k] = 2`).
# - Loop:
#   - `curr_sum = -1 + (-1) + 2 = 0`. Valid triplet: `[-1, -1, 2]`. Append it.
#   - Skip duplicates: `nums[j] = -1`, `nums[j+1] = 0`, no duplicate for `j`. For `k`, `nums[5] = 2`, `nums[4] = 1`, no duplicate.
#   - Move pointers: `j = 3`, `k = 4`.
#   - `curr_sum = -1 + 0 + 1 = 0`. Valid triplet: `[-1, 0, 1]`. Append it.
#   - Skip duplicates: `nums[3] = 0`, `nums[4] = 1`, no duplicate for `j`. For `k`, only one element left.
#   - Move pointers: `j = 4`, `k = 3`. Since `j > k`, exit loop.

# This finds both triplets for `i = 1`. The process repeats for other `i` values.

# ### Key Points
# - The two pointers `j` and `k` work together to find pairs summing to `-nums[i]` in the sorted subarray.
# - Moving `j` right or `k` left adjusts the sum based on whether it’s too small or too large.
# - Duplicate skipping ensures unique triplets.
# - The technique is efficient (O(n) per `i`, O(n²) overall) and guarantees all valid triplets are found.

# Does this clarify the two-pointer part? Want to walk through another example or focus on a specific aspect, like duplicate handling or pointer movement?