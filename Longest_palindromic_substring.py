# Given a string s, return the longest palindromic substring in s.


# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.



# NOTE: This solution works, but is definitely not the most efficient method of solving this. 
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Instantiate two pointers. 
        L, R = 0, 1

        # We take the first string as the max palindromic substring
        sub_str = s[L]

        # If the whole string is a palindrome, return it. 
        if self.isPalindrome(s):
            return s


        while (L < R) and (R < len(s)):
            # Get a sub string 
            new_sub = s[L: R + 1]

            if (self.isPalindrome(new_sub)) and (len(new_sub) > len(sub_str)):
                sub_str = new_sub 

            # If R is at the last character
            if R == len(s) - 1:
                # Move the left pointer
                L += 1
                # Reset R to (L)
                R = L 

            # Increment R
            R += 1

        return sub_str
            


    def isPalindrome(self, s: str)-> bool:
        return (s == s[::-1])        
    

# From the leetcode blog, one of the methods of solving this is:

# A common mistake:
# Some people will be tempted to come up with a quick solution, which is unfortunately flawed (however can be corrected easily):

# Reverse S and become S’. Find the longest common substring between S and S’, which must also be the longest palindromic substring.
# This seemed to work, let’s see some examples below.

# For example,
# S = “caba”, S’ = “abac”.
# The longest common substring between S and S’ is “aba”, which is the answer.

# Let’s try another example:
# S = “abacdfgdcaba”, S’ = “abacdgfdcaba”.
# The longest common substring between S and S’ is “abacd”. Clearly, this is not a valid palindrome.

# We could see that the longest common substring method fails when there exists a reversed copy of a non-palindromic substring in some other part of S. To rectify this, each time we find a longest common substring candidate, we check if the substring’s indices are the same as the reversed substring’s original indices. If it is, then we attempt to update the longest palindrome found so far; if not, we skip this and find the next candidate.

# Is this part correct?

# example string: abcxycba
# reverse string: abcxycba

# The substring indices are same as reversed string original indices and yet it is not a palindrome?


# NOTE: HERE are some alternative ways of solving it by COPILOT

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         """
#         Expand around centers approach
#         Time: O(n²), Space: O(1)
#         """
#         if not s:
#             return ""
        
#         start = 0
#         max_len = 1
        
#         for i in range(len(s)):
#             # Check for odd-length palindromes (center at i)
#             len1 = self.expand_around_center(s, i, i)
            
#             # Check for even-length palindromes (center between i and i+1)
#             len2 = self.expand_around_center(s, i, i + 1)
            
#             # Get the maximum length palindrome centered here
#             current_max = max(len1, len2)
            
#             # Update global maximum if we found a longer palindrome
#             if current_max > max_len:
#                 max_len = current_max
#                 start = i - (current_max - 1) // 2
        
#         return s[start:start + max_len]
    
#     def expand_around_center(self, s: str, left: int, right: int) -> int:
#         """
#         Expand around center and return length of palindrome
#         """
#         while left >= 0 and right < len(s) and s[left] == s[right]:
#             left -= 1
#             right += 1
        
#         # Return length of palindrome
#         return right - left - 1


# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         """
#         Dynamic Programming approach
#         Time: O(n²), Space: O(n²)
#         """
#         n = len(s)
#         if n == 0:
#             return ""
        
#         # dp[i][j] = True if s[i:j+1] is palindrome
#         dp = [[False] * n for _ in range(n)]
#         start = 0
#         max_len = 1
        
#         # Every single character is a palindrome
#         for i in range(n):
#             dp[i][i] = True
        
#         # Check for 2-character palindromes
#         for i in range(n - 1):
#             if s[i] == s[i + 1]:
#                 dp[i][i + 1] = True
#                 start = i
#                 max_len = 2
        
#         # Check for palindromes of length 3 and more
#         for length in range(3, n + 1):
#             for i in range(n - length + 1):
#                 j = i + length - 1
                
#                 # Check if s[i:j+1] is palindrome
#                 if s[i] == s[j] and dp[i + 1][j - 1]:
#                     dp[i][j] = True
#                     start = i
#                     max_len = length
        
#         return s[start:start + max_len]

# Test cases
sol = Solution()
print(sol.longestPalindrome("babad"))  # Expected: "bab" or "aba"
print(sol.longestPalindrome("cbbd"))   # Expected: "bb"
print(sol.longestPalindrome("a"))      # Expected: "a"
print(sol.longestPalindrome("ac"))     # Expected: "a" or "c"