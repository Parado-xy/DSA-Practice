/*
Problem: Maximum Sum of Subarray with Size Constraints

You are given an array of positive integers `arr` and two integers, `k` and `m`.
 Your task is to find the maximum sum of any contiguous subarray of length `k` where the sum of the subarray is less than or equal to `m`.
  If no such subarray exists, return `-1`.

Input:
- `arr`: an array of positive integers.
- `k`: an integer representing the size of the subarray.
- `m`: an integer representing the maximum allowable sum of the subarray.

Output:
- The maximum sum of any subarray of size `k` such that the sum is less than or equal to `m`.
- Return `-1` if no such subarray exists.

Constraints:
- 1 ≤ k ≤ n ≤ 10^5
- 1 ≤ arr[i] ≤ 10^4
- 1 ≤ m ≤ 10^9

Example:

Input:
arr = [1, 3, 2, 5, 8, 6]
k = 3
m = 10

Output:
10

Explanation:
The subarrays of size 3 are:
- [1, 3, 2] with sum 6
- [3, 2, 5] with sum 10
- [2, 5, 8] with sum 15 (exceeds m, so it’s not valid)
- [5, 8, 6] with sum 19 (exceeds m, so it’s not valid)

The maximum valid sum that is less than or equal to m is 10.

Approach Hints:
1. **Sliding Window for Maximum Sum:**
   - Use a sliding window of size `k` to iterate through the array and compute sums efficiently.
   
2. **Keep Track of Maximum Valid Sum:**
   - Track the maximum sum found that is less than or equal to `m`.

This problem requires efficiently finding the maximum sum while adhering to the size and sum constraints using sliding window techniques.
*/

function maximum_sub_array(arr, k, m){
   // Check if the array is smaller than the sliding window so we can just return. 
   if(arr.length < k) return -1


   // Set up pointers. 
   let pointer1 = 0
   let pointer2 = k
   //Initialize sum for storing the first sum
   let sum = 0
   // Let's get the sum of the first k
   for(let i = 0; i < k; i++){
      sum += arr[i] 
   }

   // Initialize maxSum with the first sum.
   let maxSum = {'ans': sum}

   while(pointer2 < arr.length){
      // slide the window
      let newSum = sum - arr[pointer1] + arr[pointer2]
      // Check if the new sum value is larger than the previous one, but <= m
      if(newSum > sum && newSum <= m){
         maxSum['ans'] = newSum
         sum = newSum
      }
      // Update the sum variable.
         sum = newSum
      

      // Move the pointers. 
      pointer1++
      pointer2++

   }

   return maxSum['ans'] <= m ? maxSum : -1   
}

console.log(maximum_sub_array([1, 2,3,4,5,6], 3, 10))