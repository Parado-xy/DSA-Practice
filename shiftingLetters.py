# Problem: Shifting Letters (Similar to a LeetCode problem)
# You are given a string `s` and an array `shifts` where `shifts[i]` represents 
# how many positions we should shift the i-th letter of the string. 
# After shifting, a letter wraps around if necessary (i.e., shifting 'z' by 1 gives 'a').
# We need to apply the shifts efficiently, ensuring that each character's shift 
# is cumulative and that characters are processed in constant time.

# Example:
# Input: s = "abc", shifts = [3, 5, 9]
# Output: "rpl"

class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        # Initialize a variable to store the cumulative shift amount
        total_shift = 0
        
        # Convert the string `s` into a list of characters
        # Reason: strings in Python are immutable, so converting to a list allows us to modify it in-place
        s = list(s)
        
        # Step 1: Traverse the `shifts` array in reverse order.
        # We traverse in reverse because shifts[i] affects all characters from position `i` to the end.
        for i in range(len(s) - 1, -1, -1):
            # Step 2: Accumulate the shifts from right to left.
            # Each character is shifted by the sum of all shifts from its position to the end.
            total_shift = (total_shift + shifts[i]) % 26
            
            # Step 3: Shift the current character.
            # We calculate the new position by adding the total_shift to the current character's 
            # position in the alphabet, and then use modulo 26 to wrap around the alphabet.
            # `ord(s[i]) - ord('a')` gives the current character's position in the alphabet (0 for 'a', 25 for 'z').
            # We then add the total shift and wrap it using `% 26` to ensure we stay within alphabet bounds.
            # Finally, we convert it back to a character using `chr()`.
            s[i] = chr((ord(s[i]) - ord('a') + total_shift) % 26 + ord('a'))
        
        # Step 4: Join the list back into a string and return the result.
        return ''.join(s)

# Explanation of key steps:
# - `total_shift` keeps track of the cumulative shift applied to each character.
# - The reverse traversal ensures that each character is shifted by the correct cumulative amount.
# - Using modulo 26 allows wrap-around behavior for the alphabet, so 'z' can shift to 'a', etc.

# Example Usage:
s = "abc"
shifts = [3, 5, 9]
solution = Solution()
result = solution.shiftingLetters(s, shifts)  # Expected output: "rpl"
print(result)
