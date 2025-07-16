/*
  One Away: There are three types of edits that can be performed on strings: insert a character, 
remove a character, or replace a character. Given two strings, write a function to check if they are 
one edit (or zero edits) away. 
 */




const abs = require('./eloquent').abs

function oneWay(target, str1){
    // If zero edits away (target == str1)
    if(target == str1){
        return true
    }

    // If either target or str1 is an empty string, return false
    if((target.length || str1.length) == 0){
        return false
    }

    function insertion(target, str1){

        function insertCharAt(str, char, index) {
            // If index is out of bounds, return the original string
            if (index < 0 || index > str.length) {
                return str;
            }
            
            // Slice the string into two parts and insert the character in between
            let newStr = str.slice(0, index) + char + str.slice(index);
            return newStr;
        }


        if(abs(target.length - str1.length) == 1){
            for (let i = 0; i < target.length; i++){
                for(let j = 0; j < str1.length; j++){
                    let newStr = insertCharAt(target, str1[j], i)
                    if(newStr == str1){
                        return true
                    }
                }
            }
        }
        return false
    }


    function deletion(target, str1){
        if(abs(target.length - str1.length) == 1){
            function deleteCharAt(str, index) {
                // If index is out of bounds, return the original string
                if (index < 0 || index >= str.length) {
                    return str;
                }
                
                // Slice the string into two parts and skip the character at the specified index
                let newStr = str.slice(0, index) + str.slice(index + 1);
                return newStr;
            }


                for(let j = 0; j < target.length; j++){
                    let newStr = deleteCharAt(target,  j)
                    if(newStr == str1){
                        return true
                    }
                }


        }
        return false
    }

    function replaceOperation(target, str1){
        if(target.length == str1.length){
            function replaceCharAt(str, char, index) {
                // If index is out of bounds, return the original string
                if (index < 0 || index >= str.length) {
                    return str;
                }
                
                // Replace the character at the specified index by slicing around it
                let newStr = str.slice(0, index) + char + str.slice(index + 1);
                return newStr;
            }

            for (let i = 0; i < target.length; i++){
                for(let j = 0; j < str1.length; j++){
                    let newStr = replaceCharAt(target, str1[j], i)
                    if(newStr == str1){
                        return true
                    }
                }
            }
        }
        return false
    }

    return [replaceOperation(target, str1), deletion(target, str1), insertion(target, str1)].includes(true)
    
}

console.log(oneWay('card','care'))