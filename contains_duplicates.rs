use std::collections::HashSet;

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut set = HashSet::new(); // Create an empty HashSet
        
        for num in nums { // Iterate over the vector, taking ownership of each `num`
            if !set.insert(num) { // Try to insert `num` into the set
                return true; // If insertion fails → duplicate found
            }
        }
        
        false // No duplicates after iterating all elements
    }
}