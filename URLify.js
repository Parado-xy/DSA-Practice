// URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string 
// has sufficient space at the end to hold the additional characters, and that you are given the "true" 
// length of the string. (Note: If implementing in Java, please use a character array so that you can 
// perform this operation in place.) 
// EXAMPLE 
// Input: "Mr John Smith  " 
// Output: "Mr%20John%20Smith" 

// SOLUTION:

// From what i can see, we don't really need the leading and trailing white spaces, but let's ask ChatGPT to properly descrivbe the question. 

function urlify(string){
    string = string.trim()
    let charArray = string.split('')
    for(let i = 0; i < charArray.length; i++){
            if(charArray[i] == ' '){
                charArray[i] = '%20'
            }
        
    }return charArray.join('')
}

console.log(urlify('I am a Boy    '))