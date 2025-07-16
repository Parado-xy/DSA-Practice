function twoSum(nums, target){
    // Define a Hash Map
    let hash = {}
    for(let i = 0; i < nums.length; i++){
        // Get the difference between the target and the current value
        let num = target - nums[i]
        // If the difference is already in the hash map,
        if(hash.hasOwnProperty(`${num}`)){
            
            // It means we've see the number that when added to num[i] gives target
            return [hash[`${num}`], i]
        }
            // If we've not seen it before, store the value and 
            // its index in the hash map. 
            hash[`${nums[i]}`] = i

    }
    return null
}
// To conseptualize, what we just did in the 2 sum is a follows:
// let y be the target, and x be the current value at index i.
//  z = y - x, z is the value we need to add to x to get y. 
// When we compute z, and if it's in the hashmap, it means we've encountered the
// value added to x to get y, so we can return the index of both, else
// if we've not found it, add x to the hashmap and go again. 

function isValidString(s){
  let  openingSquare = '[';
  let  closingSquare = ']';
  let  openingCurly = '{';
  let  closingCurly = '}';
  let  openingCurved = '(';
  let  closingCurved = ')';

  let count = 0;
  let valid = true

  while(count + 1 < s.length){
    if (s[count] == openingSquare){
        if(s[count + 1] == (closingCurly) || s[count + 1] ==(closingCurved)){
            valid = false
        }
    }else if(s[count] == openingCurved){
        if(s[count + 1] == (closingCurly) ||s[count + 1] == (closingSquare)){
            valid = false
        }
    }else if(s[count] == openingCurly){
        if(s[count + 1] == (closingCurved) ||s[count + 1] == (closingSquare)){
            valid = false
        }
    }

    if (!valid){
        return false
    }count += 1;
  } 

    return true
}

console.log(isValidString("()[]{}"))