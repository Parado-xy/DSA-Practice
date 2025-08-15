# Given an integer n, return true if it is a power of four. Otherwise, return false.

# An integer n is a power of four, if there exists an integer x such that n == 4x.

 

# Example 1:

# Input: n = 16
# Output: true
# Example 2:

# Input: n = 5
# Output: false
# Example 3:

# Input: n = 1
# Output: true
 

# Constraints:

# -231 <= n <= 231 - 1

import math 

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Negative numbers are out here. 
        if n < 1:
            return False
        if n == 1:
            return True
        
        log_base_4_n = math.log(n) / math.log(4) 
        # for num in range(1, int(n**(0.5))):
        #     if 4**(num) == n:
        #         return True 
        
        return True if log_base_4_n % 1 == 0 else False

# NOTE: This works for confirming if any n is a power of any x 