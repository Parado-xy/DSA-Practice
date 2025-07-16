/*
Problem: Maximum Average Subarray with Threshold

You are given an array of integers `arr` and two integers, `k` and `t`, where:
- `k` is the size of the sliding window.
- `t` is a threshold value.

Your task is to find the maximum possible average of any subarray of size `k` such that the average is 
greater than or equal to `t`. If no such subarray exists, return `-1`.

You must optimize the solution using binary search to find the highest possible valid average efficiently, 
while using the sliding window technique to check subarray sums.

Input:
- `arr`: an array of integers.
- `k`: an integer representing the size of the sliding window.
- `t`: an integer representing the threshold.

Output:
- A floating-point value representing the maximum average of any subarray of size `k` that meets the condition.
- Return `-1` if no such subarray exists.

Constraints:
- 1 ≤ k ≤ n ≤ 10^5
- -10^4 ≤ arr[i] ≤ 10^4
- -10^4 ≤ t ≤ 10^4

Example:

Input:
arr = [3, -1, 4, 1, 5, 9, -2, 6, 5]
k = 3
t = 2

Output:
5.333

Explanation:
The subarray [9, -2, 6] has an average of 4.333, and the subarray [5, 9, -2] has an average of 5.333. 
The highest possible average greater than or equal to `t` is 5.333.

Approach Hints:
1. Binary Search for Maximum Average:
   - Apply binary search to guess the possible maximum average value between the minimum and maximum values 
     of the array. The search space will be floating-point values.
   
2. Sliding Window for Validation:
   - For each guessed average from the binary search, use the sliding window technique to check whether there 
     is a subarray of size `k` with an average greater than or equal to that guess.
   - Convert the average check to a sum check using the formula:
     sum of elements in the window ≥ k * guess

This ensures the sliding window can verify the condition in constant time.
*/

