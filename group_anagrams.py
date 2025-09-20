# Group Anagrams
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.




from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a default dict with lists as values. 
        res = defaultdict(list)
        # For a string in the strings array
        for s in strs:
            # Get an array containing all zeroes. 
            count = [0] * 26
            # For charcater in string. 
            for c in s:
                # Got to that character and increment the count
                count[ord(c) - ord('a')] += 1
            # make the array hashable by converting it to a tuple
            # Make the tuple a key, and add 's' as the string to the list. 
            res[tuple(count)].append(s)
        # Return a list of all the values. 
        return list(res.values())
    
# Time & Space Complexity
# Time complexity: 
# O(m∗n)
# Space complexity:
# O(m) extra space.
# O(m∗n) space for the output list.