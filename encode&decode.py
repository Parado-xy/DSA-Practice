from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings into a single string.
        Each string is encoded as: [length of string]©[actual string]
        
        Args:
            strs: List of strings to encode
            
        Returns:
            A single string containing all encoded strings
        """
        # Initialize empty result string
        result = ''

        # Iterate through each string in the input list
        for string in strs:
            # Encode each string as [length]©[string] and add to result
            result += f"{len(string)}©{string}"

        return result 

    def decode(self, s: str) -> List[str]:
        """
        Decodes a single string back into the original list of strings.
        
        Args:
            s: Encoded string following the [length]©[string] pattern
            
        Returns:
            The original list of strings
        """
        # Initialize result list and start index
        res, i = [], 0

        # Continue until we've processed the entire string
        while i < len(s):
            # Find the © delimiter
            j = i
            while s[j] != "©":
                j += 1
                
            # Extract the length of the next string
            length = int(s[i:j])
            
            # Extract the string using the length and append to result
            res.append(s[j + 1 : j + length + 1])
            
            # Update index to point to the start of the next encoded string
            i = j + 1 + length
        
        return res
    
    def process(self, strs: List[str]) -> List[str]:
        """
        Utility method to encode and then decode a list of strings.
        Useful for testing the correctness of the encode/decode methods.
        
        Args:
            strs: List of strings to process
            
        Returns:
            The same list after encoding and decoding
        """
        return self.decode(self.encode(strs))

# Test the solution with a sample list of strings
sol = Solution().process(["She","Is","a","Lady"])
print(sol)  # Should print ['She', 'Is', 'a', 'Lady']
