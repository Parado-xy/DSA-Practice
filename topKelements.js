class Solution {
  /**
   * @param {number[]} nums
   * @param {number} k
   * @return {number[]}
   */
  topKFrequent(nums, k) {
    // Let's start with a solution that works.

    // First, let's sort the values in the array so that we have the advantage of order.
    nums.sort((a, b) => a - b);

    // Create a Pointer that Points to the current value;
    let current = nums[0];

    // Create a count for each value
    let count = 0;

    // An array to store value-frequency pairs;
    let frequency = [];
    // Let's iterate through the array, and count the occurence of each value.
    for (let i = 0; i < nums.length; i++) {
      if (nums[i] == current) {
        count++;
      } else {
        frequency.push([current, count]);
        // reset the count & current values;
        current = nums[i];
        count = 0;
        // decrement i
        i--;
      }
    }
    // Push the Last current,count pair into the frequency array;
    frequency.push([current, count]);

    // Sort the frequency array;
    frequency.sort((a, b) => b[1] - a[1]);

    return frequency.slice(0, k).map((element) => element[0]);
  }

  topKFrequentImproved(nums, k) {
    const freqMap = new Map();

    // Count frequencies
    for (const num of nums) {
      freqMap.set(num, (freqMap.get(num) || 0) + 1);
    }

    // Convert to array and sort by frequency
    const sorted = Array.from(freqMap.entries()).sort((a, b) => b[1] - a[1]);

    // Return top k elements
    return sorted.slice(0, k).map(([num]) => num);
  }
}

let ans = new Solution().topKFrequentImproved([1, 3, 3, 3, 2, 2], 2);
console.log(ans);
