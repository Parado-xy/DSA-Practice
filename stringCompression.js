/**
 *  Implement a method to perform basic string compression using the counts 
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the 
"compressed" string would not become smaller than the original string, your method should return 
the original string. You can assume the string has only uppercase and lowercase letters (a - z)
 */



function compress(string){
   // Initialize a hash map for storage.  
   let  hash = {}
   // Get the initial value
   let  prev = string[0]
   // create unique identifier so that the same letter at different points can be stored differently.
   let identifier = 1
   // Initialize the hash map with thee first letter and a count of 1.
   hash[`${prev}_${identifier}`] = 1
   // Loop through every letter in the string aside the first. 
    for(let i = 1; i < string.length; i++){
        // Check if previous letter is the same as the next
        if(prev == string[i]){
            // if they are increment the letter's count by 1 witht the same identifier
            hash[`${prev}_${identifier}`] += 1
            // set the current string to the previous one. 
            prev = string[i]
            // else if the previous letter is not the same as the next
        }else{
            // Update the identifier.
            identifier++ 
            // update the previous string. 
            prev = string[i]
            // store new occurence with a new identifier and initialize to 1.
            hash[`${prev}_${identifier}`] = 1
        }
    }
    // Create an empty string
    let ansString = ''
    // Loop through hashmap property names
    for(let key of Object.keys(hash)){
        // add each property name or key and their value to a string.
        ansString += key[0] + hash[key]
    }
    // return that string if it is shorter than the original.
     
    return ansString.length > string.length ? string : ansString
}


console.log(compress('aaaabAsaaAAAAcccc'))
console.log(...'aaaabAsaaAAAAcccc')