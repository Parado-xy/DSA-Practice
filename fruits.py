from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        Sliding window with at most 2 different fruit types
        Time: O(n), Space: O(1)
        """
        if not fruits:
            return 0
        
        left = 0
        max_fruits = 0
        fruit_count = {}  # Track count of each fruit type in current window
        
        for right in range(len(fruits)):
            # Add current fruit to window
            fruit_count[fruits[right]] = fruit_count.get(fruits[right], 0) + 1
            
            # If we have more than 2 fruit types, shrink window
            while len(fruit_count) > 2:
                fruit_count[fruits[left]] -= 1
                if fruit_count[fruits[left]] == 0:
                    del fruit_count[fruits[left]]
                left += 1
            
            # Update maximum fruits collected
            max_fruits = max(max_fruits, right - left + 1)
        
        return max_fruits

# Test cases
sol = Solution()
print(sol.totalFruit([1,2,1]))      # Expected: 3
print(sol.totalFruit([0,1,2,2]))    # Expected: 3
print(sol.totalFruit([1,2,3,2,2]))  # Expected: 4
print(sol.totalFruit([3,3,3,1,2,1,1,2,3,3,4]))  # Expected: 5