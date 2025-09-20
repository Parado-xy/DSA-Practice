# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Get a dictionary to count the numbers.

        count = {}

        # For each number
        for num in nums:
            # Upsert the count of the num. 
            count[num] = 1 + count.get(num, 0) 

        # Get an array to hold character counts. 
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        # Sort the array. 
        # Defaults to sorting via the first index.
        # Sorts in ascending order: smallest first. 
        arr.sort()

        res = []

        # While we've not reached k amount
        while len(res) < k:
            # remove/pop elements from the list
            res.append(arr.pop()[1])
        return res 
    
 
    def topKFrequentBucketSort(self, nums: List[int], k: int) -> List[int]:
        # Get a dict to store the value-count pairs. 
        count = {}
        # Create a frequency bucket. 
        freq = [[] for i in range(len(nums) + 1)]
        # For number in the numbers array. 
        for num in nums:
            # Upsert the count of that number
            count[num] = 1 + count.get(num, 0)
        
        # for items in the count dict, 
        for num, cnt in count.items():
            # Store items in the frequency list based on their indeces
            freq[cnt].append(num)

        # Create a response array. 
        res = []
        # Iterating from the last element that is guranteed to hold the most frequent. 
        for i in range(len(freq) - 1, 0, -1):
            # For number in the list at that position 
            for num in freq[i]:
                # apprnd it to the response array.
                res.append(num)

                # If the length of the response array equals k, return the response
                # Length eventually equals k. 
                if len(res) == k:
                    return res