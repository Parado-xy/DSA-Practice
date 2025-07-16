export class Solution {
  /**
   * @param nums: An integer array
   * @return: Minimum number of operations to make nums equal to 0
   */
  minimumOperations(nums) {
    // write your code here

    // Sort the array;
    nums = nums.sort((a, b) => a - b);
    // current index;
    let current = nums[0];
    // Count the number of times we've done this;
    let count = 0;

    while (nums[nums.length - 1] != 0) {
      if (current == 0) {
        current = nums[count + 1]
        continue
      }; 
      for (let i = 0; i < nums.length; i++) {
        if(nums[i] == 0) continue; 
        nums[i] = nums[i] - current;
        console.log(nums);
      }
      count++;
      current = nums[count];
    }

    return count;
  }

  minimumOperationsv2(nums){
    let uniqueValues = new Set(nums); // Create a set of unique values; 

    // If we've got the value 0 in the set, we need to make set.length - 1 operations to get everything to zero; 
    let ans = uniqueValues.size
    // This is because 
    // if we had the values in a sorted array like so:  [0, 1, 3, 5]
    // If we decide to subtract each element from the start of the array to the end by every other element
    // we'd decrease all the values of the array each time, but we would still need to touch each `unique` element in the array at least Once
    // [0, 1, 3, 5]
    // [0, 0, 2, 4] (we subtracted the element at index 1 )
    // [0, 0, 0, 2] (we subtracted the element at index 2 )
    // [0, 0, 0, 0] (we subtracted the element at index 3 )
    // We had to touch all the elements but we ignored the initial zero 
    // the answer was therefore uniqueValues.size (or uniqueValues.size - 1 if we had a value of zero in our unique values array)

    if(uniqueValues.has(0)) ans -= 1; 

    return ans
  }
}

const solution = new Solution().minimumOperationsv2([1, 5, 0, 3, 5]);
console.log(solution);
