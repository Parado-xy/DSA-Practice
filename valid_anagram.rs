// Check if two strings are anagrams of each other;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false;
        }

        let mut counts = [0; 26]; // Create a mutable array of counts in the repeating syntax;

        // Iterate through characters directly (O(n) time)
        for (s_char, t_char) in s.chars().zip(t.chars()) {
            // Check if characters are valid lowercase a-z
            if !s_char.is_ascii_lowercase() || !t_char.is_ascii_lowercase() {
                return false;
            }

            // Calculate indices safely
            let s_idx = s_char as usize - 'a' as usize;
            let t_idx = t_char as usize - 'a' as usize;

            counts[s_idx] += 1;
            counts[t_idx] -= 1;
        }

        // Check all counts are zero
        counts.iter().all(|&x| x == 0)
    }
}