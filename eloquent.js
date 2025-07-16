// Note that enquoting your string in back ticks (``) can be seen as 
// Python's version of tripple quotes and can span multiple lines.
// The way strings are ordered is roughly alphabetic but not really what you’d expect to see in a
// dictionary: uppercase letters are always “less” than lowercase ones, so "Z" < "a", and nonalphabetic
// characters (!, -, and so on) are also included in the ordering. When comparing strings, JavaScript
// goes over the characters from left to right, comparing the Unicode codes one by one.

// When comparing values of the same type using ==, the outcome is easy to predict: you should get
// true when both values are the same, except in the case of NaN. But when the types differ, JavaScript
// uses a complicated and confusing set of rules to determine what to do. In most cases, it just tries to
// convert one of the values to the other value’s type. However, when null or undefined occurs on either
// side of the operator, it produces true only if both sides are one of null or undefined.

/**
 * JavaScript's `forEach` method is used to execute a provided function once for each array element. It's a convenient way to iterate over arrays without using a traditional `for` loop.

Here's a basic example:

```javascript
const array = [1, 2, 3, 4, 5];

array.forEach((element) => {
    console.log(element);
});
```

In this example, the `forEach` method calls the provided function once for each element in the array, logging each element to the console.

### Key Points:
- **Callback Function**: The function you pass to `forEach` is called a callback function. It takes three arguments:
  1. **Current Value**: The current element being processed in the array.
  2. **Index** (optional): The index of the current element.
  3. **Array** (optional): The array `forEach` was called upon.

- **No Return Value**: `forEach` does not return a new array or any value. It simply executes the callback function for each element.

- **Cannot Break**: Unlike a `for` loop, you cannot break out of a `forEach` loop. If you need to stop the iteration based on a condition, consider using a `for` loop or the `some` method.

Here's an example using all three arguments:

```javascript
const array = ['a', 'b', 'c'];

array.forEach((element, index, arr) => {
    console.log(`Element: ${element}, Index: ${index}, Array: ${arr}`);
});
```

This will output:
```
Element: a, Index: 0, Array: a,b,c
Element: b, Index: 1, Array: a,b,c
Element: c, Index: 2, Array: a,b,c
```

Note that when writing switch statements in javascript, you have to write a break statement after every case statement.
example: 

weather = String(prompt('How's the weather today? '))

switch weather{
    case 'rainy':
      console.log('Take an Umbrella!)
      break;
    case 'sunny':
      console.log('Play Video Games')
      break;
    default:
      console.log('Sleep')
      break;    
}
 */

/** LOOPING A TRIANGLE */
/**
 * for(let i = '#'; i.length < 8; i += '#'){
  console.log(i)
} */


/**FizzBuzz
 * Write a program that uses console.log to print all the numbers from 1 to 100,
 with two exceptions. For numbers divisible by 3, print "Fizz" instead of the
 number, and for numbers divisible by 5 (and not 3), print "Buzz" instead.
 When you have that working, modify your program to print "FizzBuzz" for
 numbers that are divisible by both 3 and 5 (and still print "Fizz" or "Buzz"
 for numbers divisible by only one of those).


for(let i = 1; i <= 100; i++){
  if(i % 3 == 0){
    console.log('Fizz')
    // Additional conditional for numbers divisible by both 3 and 5
    if(i % 5 == 0) console.log('FizzBuzz')
  }else if(i % 5 == 0 && i % 3 != 0){
    console.log('Buzz')
  }else{
    console.log(i)
  }
} 

 */
/** Chess Board 
 *  Write a program that creates a string that represents an 8×8 grid, using newline
 characters to separate lines. At each position of the grid there is either a space
 or a "#" character. The characters should form a chessboard.
 Passing this string to console.log should show something like this:
  # # # #
 # # # #
  # # # #
# # # #
  # # # #
 # # # #
  # # # #
 # # # #
*/
board = ''
for(let i = 1; i <= 8; i++){
  for(let j = 1; j <= 8; j++){
    if((j + i) % 2 != 0){
      board += ' '
    }else{
      board += '#'
    }
  }
  // Add the required line break. 
  board += '\n'
}
// Log the board into the console.
// console.log(board)

/**
 * Rounds a number to the nearest multiple of a given step.
 *
 * @param {number} n - The number to be rounded.
 * @param {number} step - The step to which the number should be rounded.
 * @returns {number} - The number rounded to the nearest multiple of the step.
 *
 * @example
 * // Rounds 7 to the nearest multiple of 5
 * roundTo(7, 5); // returns 5
 *
 * @example
 * // Rounds 12 to the nearest multiple of 4
 * roundTo(12, 4); // returns 12
 *
 * @example
 * // Rounds 15 to the nearest multiple of 6
 * roundTo(15, 6); // returns 18
 */
const roundTo = (n, step) => {
  let remainder = n % step;
  // This next line does the rounding up or rounding down. 
  // If the remainder is less than the step, it's rounded down, else it is rounded up
  return n - remainder + (remainder < step / 2 ? 0 : step);
};

/**
 * A **closure** is a feature in JavaScript (and many other programming languages) where an inner function has access to the outer (enclosing) function's variables. This includes:

1. **Variables declared in the outer function's scope**.
2. **Variables declared in the global scope**.

Closures are created every time a function is created, at function creation time.

### How Closures Work in JavaScript

Here's a simple example to illustrate closures:

```javascript
function outerFunction(outerVariable) {
    return function innerFunction(innerVariable) {
        console.log('Outer Variable:', outerVariable);
        console.log('Inner Variable:', innerVariable);
    };
}

const newFunction = outerFunction('outside');
newFunction('inside');
```

In this example:
- `outerFunction` is an outer function that takes one argument `outerVariable`.
- `innerFunction` is an inner function that takes one argument `innerVariable` and logs both `outerVariable` and `innerVariable`.
- When `outerFunction` is called with the argument `'outside'`, it returns `innerFunction`.
- `newFunction` is now a reference to `innerFunction`, but it still has access to `outerVariable` from `outerFunction`'s scope.

### Why Are Closures Useful?

Closures are useful because they allow you to:
1. **Encapsulate**: Create private variables that can only be accessed by the inner function.
2. **Maintain State**: Preserve data across function calls.

### Practical Example

A common use case for closures is to create functions with private variables:

```javascript
function createCounter() {
    let count = 0;
    return function() {
        count++;
        return count;
    };
}

const counter = createCounter();
console.log(counter()); // 1
console.log(counter()); // 2
console.log(counter()); // 3
```

In this example:
- `createCounter` is an outer function that initializes a private variable `count`.
- It returns an inner function that increments and returns `count`.
- Each call to `counter` increments and logs the updated count, demonstrating how the inner function maintains access to the `count` variable even after `createCounter` has finished executing.

Closures are a powerful feature in JavaScript that enable more flexible and maintainable code. If you have any more questions or need further clarification, feel free to ask!
 */





/**
 * Finds two indices in a sorted array such that the elements at those indices add up to a specific target.
 *
 * @param {number[]} arr - The sorted array of numbers.
 * @param {number} target - The target sum.
 * @returns {(number[]|null)} - An array containing the two indices if a pair is found, or null if no such pair exists.
 *
 * @example
 * // Returns [1, 4] because arr[1] + arr[4] = 2 + 7 = 9
 * twoSum([1, 2, 3, 4, 7], 9);
 *
 * @example
 * // Returns null because no two numbers add up to 10
 * twoSum([1, 2, 3, 4, 7], 10);
 */
function twoSum(arr, target) {
  let low = 0;
  let high = arr.length - 1;
  for (let i = 0; i < arr.length; i++) {
    if ((arr[low] + arr[high]) == target) {
      return [low, high];
    } else if ((arr[low] + arr[high]) < target) {
      low++;
    } else {
      high--;
    }
  }
  return null;
}

/**
 * Returns the smaller of two numbers.
 *
 * @param {number} a - The first number to compare.
 * @param {number} b - The second number to compare.
 * @returns {number} - The smaller of the two numbers.
 *
 * @example
 * // Returns 3 because 3 is smaller than 5
 * min(3, 5);
 *
 * @example
 * // Returns -2 because -2 is smaller than 1
 * min(-2, 1);
 *
 * @example
 * // Returns 7 because both numbers are equal
 * min(7, 7);
 */
function min(a, b) {
  return a < b ? a : b;
}

/**
 * Determines if a number is even using a recursive approach.
 *
 * @param {number} a - The number to check.
 * @returns {boolean} - Returns true if the number is even, false if the number is odd.
 *
 * @example
 * // Returns true because 4 is even
 * isEven(4);
 *
 * @example
 * // Returns false because 5 is odd
 * isEven(5);
 *
 * @example
 * // Returns true because 0 is even
 * isEven(0);
 */
function isEven(a) {
  //Get the absolute value of a
  a = abs(a)
  // Base case for odd number
  if (a == 1) {
    return false;
  } else if (a == 0) {
    return true;
  } else {
    return isEven(a - 2);
  }
}

/**
 * Returns the absolute value of a number.
 *
 * @param {number} a - The number for which to find the absolute value.
 * @returns {number} - The absolute value of the given number.
 *
 * @example
 * // Returns 5 because the absolute value of -5 is 5
 * abs(-5);
 *
 * @example
 * // Returns 3 because the absolute value of 3 is 3
 * abs(3);
 *
 * @example
 * // Returns 0 because the absolute value of 0 is 0
 * abs(0);
 */
function abs(a) {
  return a < 0 ? -a : a;
}



/**
 * Counts the number of occurrences of a specific character in a given string.
 *
 * @param {string} string - The string in which to count the occurrences of the character.
 * @param {string} char - The character to count within the string.
 * @returns {number} - The number of times the specified character appears in the string.
 *
 * @example
 * // Returns 3 because the character 'a' appears 3 times in the string
 * countChar('banana', 'a');
 *
 * @example
 * // Returns 0 because the character 'z' does not appear in the string
 * countChar('apple', 'z');
 *
 * @example
 * // Returns 2 because the character 'l' appears 2 times in the string
 * countChar('hello', 'l');
 */
function countChar(string, char) {
  let count = 0;
  for (let i = 0; i < string.length; i++) {
    if (string[i] === char) {
      count++;
    }
  }
  return count;
}


/**
 * Generates an array of numbers starting from `start` to `stop` (inclusive) with a specified `step`.
 *
 * @param {number} [start=0] - The starting number of the sequence.
 * @param {number} end - The ending number of the sequence.
 * @param {number} [step=1] - The difference between each number in the sequence.
 * @returns {number[]} An array of numbers from `start` to `stop` with increments of `step`.
 *
 * @example
 * range(1, 5); // [1, 2, 3, 4, 5]
 * @example
 * range(0, 10, 2); // [0, 2, 4, 6, 8, 10]
 * @example
 * range(5, 1, -1); // [5, 4, 3, 2, 1]
 */
function range(start = 0, end, step = 1) {
  let result = [];
  for (let i = start; i <= end; i += step) {
    result.push(i);
  }
  return result;
}

/**
 * Calculates the sum of all elements in an array.
 *
 * @param {number[]} arr - An array of numbers.
 * @returns {number} The sum of all numbers in the array.
 *
 * @example
 * sum([1, 2, 3, 4, 5]); // 15
 * @example
 * sum([10, -2, 3.5]); // 11.5
 */
function sum(arr) {
  let result = 0;
  for (let value of arr) {
    result += value;
  }
  return result;
}

/**
 * Reverses the elements of an array and returns a new array.
 *
 * @param {Array} arr - The array to be reversed.
 * @returns {Array} - A new array with the elements of `arr` in reverse order.
 */
function reverseArray(arr) {
  // Initialize an empty array to hold the reversed elements
  let newArr = [];
  
  // Loop through the input array from the last element to the first
  for (let i = arr.length - 1; i >= 0; i--) {
    // Push the current element to the new array
    newArr.push(arr[i]);
  }
  
  // Return the new array with reversed elements
  return newArr;
}


/**
 * Reverses the elements of an array in place.
 *
 * @param {Array} arr - The array to be reversed.
 * @returns {Array} - The original array with its elements reversed.
 */
function reverseArrayInPlace(arr) {
  // Note that When the array has an odd number of elements, 
  // the middle element remains in its position because the swapping process only 
  // affects the elements before and after it. 
  // This ensures that the function works correctly for arrays of any length.

  // Loop through the first half of the array
  for (let i = 0; i < Math.floor(arr.length / 2); i++) {
    // Swap the current element with the corresponding element from the end
    let val1 = arr[arr.length - 1 - i];
    let val2 = arr[i];
    arr[i] = val1;
    arr[arr.length - 1 - i] = val2;
  }
  
  // Return the modified array
  return arr;
}

  // *******************************************************
  // LinkedList =  Nodes are in 2 parts (data + address)
  //                        Nodes are in non-consecutive memory locations
  //                        Elements are linked using pointers
            
  //    advantages?
  //    1. Dynamic Data Structure (allocates needed memory while running)
  //    2. Insertion and Deletion of Nodes is easy. O(1) 
  //    3. No/Low memory waste
  
  //    disadvantages?
  //    1. Greater memory usage (additional pointer)
  //    2. No random access of elements (no index [i])
  //    3. Accessing/searching elements is more time consuming. O(n)
  
  //    uses?
  //    1. implement Stacks/Queues
  //    2. GPS navigation
  //    3. music playlist
  // *******************************************************

function arrayToList_1(arr, next = 0){
  // Base Case. 
  if(arr[next] == undefined){
    return null
  }else{
    return {
      value : arr[next],
      rest  : arrayToList_1(arr, next+= 1)
    }
  }
}

/**
 * Converts an array to a linked list.
 *
 * @param {Array} arr - The array to be converted.
 * @param {number} [count=0] - The current index in the array (default is 0).
 * @returns {Object|null} - The linked list created from the array.
 *
 * This function works by recursively creating nodes for each element in the array.
 * Each node contains a value and a reference to the next node, forming a linked list.
 * The recursion stops when the end of the array is reached, returning null to signify
 * the end of the list.
 */
function arrayToList(arr, count = 0) {
  // Base case: if the current index is beyond the last element
  if (count >= arr.length) {
    // Return null to signify the end of the list
    return null;
  } else {
    // Create a node with the current element and a reference to the next node
    return {
      value: arr[count],
      rest: arrayToList(arr, count + 1)
    };
  }
}

/**
 * Converts a linked list to an array.
 *
 * @param {Object} list - The linked list to be converted.
 * @param {Array} [arr=[]] - The array to store the values (default is an empty array).
 * @returns {Array} - The array containing all the values from the linked list.
 *
 * This function works by recursively traversing the linked list and pushing each value
 * to the same array. Since the array is passed by reference, all modifications are made
 * to the same array, which is returned at the end.
 */
function listToArray(list, arr = []) {
  // Base case: if the current node is the last node
  if (list.rest == null) {
    // Push the value of the last node to the array
    arr.push(list.value);
  } else {
    // Push the current node's value to the array
    arr.push(list.value);
    // Recursively call listToArray with the next node and the same array
    listToArray(list.rest, arr);
  }
  // Return the array containing all the values from the linked list
  return arr;
}

/**
 * Determines if a string has all unique characters.
 * Case-insensitive: treats 'A' and 'a' as the same character.
 * 
 * @param {string} str - The input string to check for uniqueness.
 * @returns {boolean} - Returns true if all characters in the string are unique, false otherwise.
 */
function isUnique(str) {
  // Create an object to store character counts
  let count = {};
  
  // Loop through the string, checking if each character has appeared before
  for (let i = 0; i < str.length; i++) {
    let char = str[i].toLowerCase(); // Convert character to lowercase for case-insensitivity
    
    // If the character has already been encountered, return false
    if (count.hasOwnProperty(char)) {
      return false;
    }
    
    // Otherwise, mark this character as encountered
    count[char] = 1;
  }

  // If no duplicate characters were found, return true
  return true;
}

/**
 * Determines if one string is a permutation of another string.
 * A permutation means the two strings contain the same characters with the same frequency, in any order.
 * 
 * @param {string} a - The first string to compare.
 * @param {string} b - The second string to compare.
 * @returns {boolean} - Returns true if string 'a' is a permutation of string 'b', false otherwise.
 */
function isPermutation(a, b) {
  // First, check if the lengths of the two strings are equal
  if (a.length !== b.length) {
    return false;
  }

  // Create a hash map to store character counts from string 'a'
  let hash1 = {};

  // Populate hash1 with the frequency of each character in string 'a'
  for (let char of a) {
    char = char.toLowerCase(); // Convert to lowercase to ensure case-insensitivity
    // Increment the count if the character already exists, else initialize it
    hash1[char] = (hash1[char] || 0) + 1;
  }

  // Iterate through string 'b' and adjust the character counts in hash1
  for (let char of b) {
    char = char.toLowerCase(); // Case-insensitive comparison

    // If the character in 'b' is not found in 'a', or its count is already zero, return false
    if (!hash1[char]) {
      return false;
    }

    // Decrement the character count
    hash1[char]--;
  }

  // Check that all character counts have been reduced to zero
  // This confirms that the two strings have matching character frequencies
  return Object.values(hash1).every(count => count === 0);
}

/**
 * Performs a binary search on a sorted array to find the target value.
 * 
 * @param {number[]} arr - The sorted array of numbers to search through.
 * @param {number} target - The target value to find in the array.
 * @returns {number|null} - The index of the target if found, otherwise returns null.
 */
function binarySearch(arr, target) {
  let low = 0;                   // The lowest index of the search range
  let high = arr.length - 1;      // The highest index of the search range

  // Continue searching while the range is valid
  while (low <= high) {
    // Find the middle index
    let mid = Math.floor((low + high) / 2);

    // If the target is found, return the index
    if (arr[mid] == target) {
      return mid;
    }
    // If the target is greater, search the right half of the array
    else if (arr[mid] < target) {
      low = mid + 1;
    }
    // If the target is smaller, search the left half of the array
    else {
      high = mid - 1;
    }
  }

  // If the target is not found, return null
  return null;
}


function flatten(matrix){
 return matrix.reduce((a,b)=> a.concat(b))
}

/**
 * Finds the subarray of length `k` that has the maximum sum in the given array.
 * 
 * @param {number[]} arr - The input array of numbers.
 * @param {number} k - The size of the subarray window.
 * @returns {number[]} - The indices `[start, end]` of the subarray with the maximum sum.
 *                        If no valid subarray is found (e.g., if `k` is greater than the array length),
 *                        the function returns `undefined`.
 * 
 * @example
 * // Example usage:
 * const arr = [1, 2, 3, 4, 5, 6, 7];
 * const k = 3;
 * const result = maximumSubArray(arr, k); // Returns [4, 6] (sum: 18 for [5, 6, 7])
 */
function maximumSubArray(arr, k){
  let pointer1 = 0;
  let pointer2 = k;
  let sum = 0; // To store the current sum.
  let maxSum = 0;  // To store the maximum sum encountered
  let hash = {};

  // Calculate the sum of the initial window
  for(let i = 0; i < k; i++){
    sum += arr[i];
  }

  maxSum = sum;  // Initialize maxSum with the initial window sum
  hash['sum'] = [0, k - 1];  // Store the initial window indices

  // Slide the window across the array
  while(pointer2 < arr.length){
    let sum2 = sum - arr[pointer1] + arr[pointer2];  // Update the sum for the new window

    // Check if the new window sum is greater than the current maxSum
    if(sum2 > maxSum) {
      maxSum = sum2;
      hash['sum'] = [pointer1 + 1, pointer2];  // Update with the new window indices
    }

    sum = sum2;  // Update sum to the new window's sum
    pointer1++;  // Move pointers one step forward.
    pointer2++;
  }

  return hash['sum'];  // Return the indices of the window with the maximum sum
}


/**
 * Removes duplicate values from a sorted linked list.
 *
 * Given a linked list where elements are sorted in ascending order, this function removes duplicate
 * elements such that each element appears only once in the list. It modifies the list in-place and 
 * returns the modified list.
 *
 * @param {Object} linkedList - The head node of a sorted linked list.
 * @param {any} linkedList.value - The value of the current node.
 * @param {Object|null} linkedList.rest - The reference to the next node in the list, or null if it's the end.
 * @returns {Object} - The head of the modified linked list with duplicates removed.
 *
 * @example
 * // Example of a linked list: { value: 1, rest: { value: 1, rest: { value: 2, rest: null }}}
 * const linkedList = { value: 1, rest: { value: 1, rest: { value: 2, rest: null }}};
 * const result = removeDuplicateInLinkedList(linkedList);
 * // result will be { value: 1, rest: { value: 2, rest: null }}
 */
function removeDuplicateInLinkedList(linkedList) {
  // Recursive function to traverse and remove duplicates
  function search(prev, current) {
    if (current == null) {
      return; // Base case: end of the list
    }

    // If the current node is a duplicate of the previous node
    if (prev.value == current.value) {
      prev.rest = current.rest; // Skip the current node
      search(prev, current.rest); // Continue from the next node
    } else {
      search(current, current.rest); // Move to the next node
    }
  }

  // If the list is empty or has only one element, return it as is
  if (linkedList == null || linkedList.rest == null) {
    return linkedList;
  }

  // Start the search from the head of the list
  search(linkedList, linkedList.rest);

  // Return the modified list
  return linkedList;
}


/**
 * Class representing a 2D vector.
 */
class Vector {
  /**
   * Create a vector.
   * @param {number} x - The x-coordinate.
   * @param {number} y - The y-coordinate.
   */
  constructor(x, y) {
    /**
     * The x-coordinate of the vector.
     * @type {number}
     */
    this.x = x;

    /**
     * The y-coordinate of the vector.
     * @type {number}
     */
    this.y = y;
  }

  /**
   * Add another vector to this vector.
   * @param {Vector} vector - The vector to add.
   */
  add(vector) {
    this.x += vector.x;
    this.y += vector.y;
  }

  /**
   * Subtract another vector from this vector.
   * @param {Vector} vector - The vector to subtract.
   */
  subtract(vector) {
    this.x -= vector.x;
    this.y -= vector.y;
  }

  /**
   * Get the length (magnitude) of the vector.
   * @type {number}
   * @readonly
   */
  get length() {
    return Math.sqrt(this.x ** 2 + this.y ** 2);
  }
}

class Group{
    constructor(){
      this.container = []
    }

    add(element){
      if (!this.container.includes(element)){
        this.container.push(element)
      }
    }

    delete(element){
      let index = this.container.indexOf(element)
      if( index != -1){
          this.container.splice(index,1)
      }
    }

    has(element){
      return this.container.includes(element)
    }

    static from(array){
      let group = new Group()
      for(let i = 0; i < array.length; i++){
        group.add(array[i])
      }

      return group
    }
}



module.exports = {
  roundTo, twoSum, min, isEven, abs, countChar, sum, range, reverseArray, reverseArrayInPlace, 
  arrayToList, listToArray, isUnique, isPermutation, maximumSubArray, binarySearch, removeDuplicateInLinkedList,
  Vector
}
