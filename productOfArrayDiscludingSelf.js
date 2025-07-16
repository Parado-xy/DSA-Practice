class Solution {
  /**
   * @param {number[]} nums
   * @return {number[]}
   */
  productExceptSelf(nums) {
    // Get the current value;
    let output = [];

    for (let i = 0; i < nums.length; i++) {
      // calculate the product excluding the current index;
      let product = nums.reduce((prev, curr, index) => {
        // if we're about to reduce the index we're currently in,
        if (index == i) {
          //  return the previously reduced total (thereby skipping or discluding this)
          return prev;
        } else {
          // return prev * curr
          return prev * curr;
        }
      }, 1); // set the initialValue to one so the index of the method matches the general index
      // push that into the array;
      output.push(product);
    }
    return output; 
  }

  productExceptSelfEffective(nums){
    // 4, 3, 2, 1, 2
    let res = new Array(nums.length).fill(1); // [1, 1, 1, 1, 1]

    // Prefix pass; 
    // The prefix pass runs through the array and computes the product of values before the current value and excluding the current value; 
    // The response array contains the neutral placeholder `1`
    let prefix = 1; 
    for (let i = 0; i < nums.length; i++){
        res[i] = prefix; // [1, 4, 12, 24, 24]
        prefix *= nums[i]; // 24
    }

    // Postfix pass;
    // The postfix pass works on the response array containing the prefixes and multiplies the sum of all values before the current value, excluding the current value
    let postfix = 1;
    for(let i = nums.length - 1; i >= 0; i--){
        res[i] *= postfix; // [12, 16, 24, 48, 24]
        postfix *= nums[i] // 12
    }
    return res; 
  }
}

let sol = new Solution()
console.log(sol.productExceptSelfEffective([4, 3, 2, 1, 2]));
