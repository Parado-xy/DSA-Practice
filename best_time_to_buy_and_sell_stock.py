# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104




# SOLUTION

# The brute force method of a double for loop is not necessary here, and this problem is marked with dynamic programming because it requires the Sliding Window technique.

# Based on the fact that we have to sell after we buy and we are trying to maximize profit, we can iterate through the prices and only need to consider two things:
# 1.) Is this price cheaper than any other price I've seen before?
# 2.) If I subtract current price by the cheapest price I've found, does this yield a greater profit than what I've seen so far?

# A fun thing to note is if #1 is true, then #2 cannot be true as well so there isn't a need to check

# Let's consider an example of [4,1,5,2,7]

# 4 is the cheapest price we see to start, and we can't sell on the first day so maxProfit is 0
# 1 is now the cheapest price we've seen. Selling now would lose us money, so we can't update maxProfit
# 5 is not cheaper than 1, but if we sell now we get a maxProfit of 4! Better save that for later
# 2 is not cheaper than 1 and if we sell, we only get a profit of 1, no need to do anything here
# 7 is not cheaper than 1, but if we sell here, we'll increase maxProfit to 6, making this the best profit to return.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # We Can't sell in the past.
        # We can assume the best time to buy is on the first day.  
        max_profit = 0
        cheapest = prices[0]

        for index, value in enumerate(prices):
            # We can't sell on the first day. 
            if index == 0:
                continue 
            # If the current value is cheaper than the cheapest thing we've seen, we save this value. 
            if (value < cheapest):
                cheapest = value
            # Else if the current current_profit is greater than the previous max_profit, 
            elif(max_profit < value - cheapest):
                max_profit = value - cheapest

        return max_profit




            
            
        

