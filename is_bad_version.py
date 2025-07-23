# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

# Example 1:

# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.
# Example 2:

# Input: n = 1, bad = 1
# Output: 1

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def isBadVersion(val: int) -> bool:
    ...

class Solution:
    def firstBadVersion(self, n: int) -> int:

        # This can be solved using binary search 
        # If we have n versions, the first bad version could have occurred between v1 and version n; 
        L, R = 1, n

        while (L < R):
            mid = L + (R - L) // 2

            if(isBadVersion(mid)):
                # If we find the current version to be a bad version,
                # We know that it and everything after it is a bad version, 
                # But it may not necessarily be the first bad version. 

                # We cut out the right side. 
                # But because this could indeed be the first bad version, we don't exclude it.
                R = mid
            else:
                # Else if that version is not a bad version,
                # We know that every version before it is good as well, 
                # So we cut them out. 
                L = mid + 1
            

        return L
        