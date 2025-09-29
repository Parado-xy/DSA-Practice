# Question:
# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) 
# such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2]. 
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, 
# or -1 if it is not in nums.

# User's Solution:
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # Function to find the pivot where rotation happens
        def find_pivot(arr):
            if not arr:  # Handle empty array
                return -1  

            # Loop to find where the order is violated
            for i in range(1, len(arr)):
                if arr[i] < arr[i - 1]:
                    return i  # Return the index of the pivot

            return 0  # Return 0 if no pivot is found (array is not rotated)

        # Get pivot using the helper function
        pivot = find_pivot(nums)

        # Perform binary search on the adjusted array
        L, R = 0, len(nums) - 1

        while L <= R:
            mid = L + (R - L) // 2  # Find the middle index
            real_mid = (mid + pivot) % len(nums)  # Adjust mid by the pivot
            if nums[real_mid] == target:  # Target found
                return real_mid
            elif target < nums[real_mid]:  # Target is in the left half
                R = mid - 1
            else:  # Target is in the right half
                L = mid + 1

        return -1  # Target not found

# Optimized Solution:
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # Optimized function to find the pivot using binary search
        def find_pivot(arr):
            L, R = 0, len(arr) - 1
            # Narrow down to the smallest element
            while L < R:
                mid = L + (R - L) // 2
                if arr[mid] > arr[R]:  # Pivot is in the right half
                    L = mid + 1
                else:  # Pivot is in the left half
                    R = mid
            return L  # Pivot is the smallest element's index

        # Find the pivot index
        pivot = find_pivot(nums)

        # Perform binary search adjusted for rotation
        L, R = 0, len(nums) - 1
        while L <= R:
            mid = L + (R - L) // 2  # Calculate the middle index
            real_mid = (mid + pivot) % len(nums)  # Adjust mid by the pivot
            if nums[real_mid] == target:  # Target found
                return real_mid
            elif target < nums[real_mid]:  # Target is in the left half
                R = mid - 1
            else:  # Target is in the right half
                L = mid + 1

        return -1  # Target not found
    
    def more_optimized_search(self, nums: list[int], target: int)-> int:
        # Get a pointer to the left and right. 
        L, R = 0, len(nums) - 1

        while L <= R:
            # Get a middle pointer. 
            mid = (L + R) // 2

            if target == nums[mid]:
                return mid
            
            # Left sorted portion. 
            if nums[L] <= nums[mid]:
                # If the target is greater than the current mid, or if the target is less than 
                # the least left value. 
                if target > nums[mid] or target < nums[L]:
                    # It means the target is not in the left ordered section. 
                    # So we cut it off. 
                    L = mid + 1
                else:
                    # Else if the target is not greater than the mid 
                    # and the target is not less than the least left value.
                    # We cut off the right ordered space. 
                    R = mid - 1
            else:
                # If we're in the right sorted portion of the array. 
                if target < nums[mid] or target > nums[R]:
                    # And if the target is less than the mid or the target is 
                    # greater than the greatest R,
                    # Then the solution is in the Left portion of the array 
                    # So we cut out the right. 
                    R = mid - 1
                else:
                    # If the target is in the right portion, we cut out the left portion. 
                    L = mid + 1

        # Return -1 if we find nothing.
        return -1
    
sol = Solution()
print(sol.more_optimized_search([4,5,6,7,0,1,2],  1))