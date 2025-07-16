// Title: Two Sum
// URL: https://leetcode.com/problems/two-sum/
// Difficulty: Easy
// The question is asking for the indices of two numbers that add up to a target number.

    // This is the brute force solution to the problem;
    pub fn two_sum_bf(nums: Vec<i32>, target: i32) -> Vec<i32> {
        for (i, item) in nums.iter().enumerate(){
            let needed = target - item;
            let probable_ans = nums.iter().enumerate().find(|&(index, &x)| x == needed && index != i);

            if let Some((j,_)) = probable_ans{
                return vec![j as i32, i as i32];
            }else{
               continue;  
            }
        }

        vec![]
    }

    // This is the optimized solution to the problem;
    use std::collections::HashMap;

    impl Solution {
        pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
            let mut seen = HashMap::new();
            
            for (i, &num) in nums.iter().enumerate() {
                let needed = target - num;
                
                if let Some(&j) = seen.get(&needed) {
                    return vec![j as i32, i as i32];
                }
                
                seen.insert(num, i);
            }
            
            vec![] // Problem states there's a solution, so this is just a fallback
        }
    }