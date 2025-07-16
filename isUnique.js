function isUnique(string){
    let hash = {}
    for (let char = 0; char < string.length; char++) {
        if (!hash.hasOwnProperty(string[char])) {
            hash[string[char]] = 1
        }else{
            return false
        }
    }
    return true 
}

function isUniqueWithoutAdditionalDataStructures(string){
    for(let i = 0; i < string.length; i++){
        // If j tries to get out of bounds, it is stopped. 
        for(let j = i + 1; j < string.length; j++){
            // If the string before it is ever equal to the string after it, the string is not unique. 
            if(string[i] == string[j]){
                return false
            }
        }
    }
    return true
} 

console.log(isUniqueWithoutAdditionalDataStructures('janeTran'))