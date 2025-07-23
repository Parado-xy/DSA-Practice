# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1

# This solution works, but it is O(n^2) and isn't effective. 
# It earned me a TLE

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Set a max_area variable
        max_area = 0 

        # Loop through the heights testing each one against very-other one. 
        for i in range(len(height)):
            for j in range(len(height)):

                # If we're on the same bar, skip; 
                if i == j:
                    continue 

                # Calculate the width and height
                calculated_width = (j + 1) - (i + 1)
                # Height is the minimum between 2 bars because we don't want slants. 
                calculated_height = min(height[j], height[i])
                # Calculate area; 
                area = calculated_width * calculated_height 

                # Update the maximum area variable; 
                max_area = max(max_area, area)

        return max_area
        

    # This version solved using the 2_ptr approach works, achieving good space complexity, 
    # and being fast enough to not get a TLE. 
    # The approach this one works with is that it check each index simultaneously for the highest height values. 
    # The side that changed height (whose pointer was incremented/decremented) was the side contributing to a lower area at that time. 
    # If the best height has been found, the pointer doesn't leave that position while trying every other option till it meets that same pointer. 
    # at this point, the search exits and we return the area from all our tries.      
    def maxArea_2ptr_approach(self, height: List[int]) -> int:

        # Iitialize low_ptr
        low_ptr = 0
        # Initialize high_ptr
        high_ptr = len(height) - 1

        # Set max_area
        max_area = 0

        # We loop until both pointers meet; 
        while (low_ptr < high_ptr):

            # Get the width and the Height. 
            calc_width = (high_ptr  - low_ptr )
            calc_height = min(height[high_ptr], height[low_ptr]) # We do not want slant heights so we take the lower. 
            # Calculate the area. 
            area = calc_width * calc_height 

            # Update the area. 
            max_area = max(max_area, area) 

            # Move the pointer that points to the shorter line
            if (height[high_ptr] > height[low_ptr]):
                # Increment the low_ptr
                low_ptr += 1
            else:
                # decrement the high_ptr
                high_ptr -= 1

        return max_area  


# The key insight is: moving the pointer with the larger height will never give us a better solution because:

# - Width decreases (pointers get closer)
# - Height is still limited by the shorter line
# - So area can only decrease or stay the same