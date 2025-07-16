/**
 * Problem: Binary Search on a Linked List

You are given a sorted singly linked list, where each node contains an integer value in non-decreasing order. 
Your task is to implement an algorithm to perform binary search on the linked list to determine if a given 
target value exists within the list. You can only traverse the list using pointers, and random access 
(like using indices) is not allowed.

The algorithm should return `true` if the target is found and `false` if it is not present in the list.

Constraints:
1. The linked list is sorted in non-decreasing order.
2. You must implement the search algorithm in O(log n) time, or as close as possible to logarithmic time, 
   despite the nature of a singly linked list.
3. The algorithm should traverse the linked list as efficiently as possible, without using extra memory 
   or converting the list into an array.

Example 1:
Input: Linked List: 1 -> 2 -> 4 -> 5 -> 7 -> 8 -> 10, Target: 5
Output: true (since 5 is in the list)

Example 2:
Input: Linked List: 1 -> 2 -> 4 -> 5 -> 7 -> 8 -> 10, Target: 6
Output: false (since 6 is not in the list)

Your task is to come up with a method to simulate binary search in a singly linked list by identifying 
the middle element, comparing it with the target, and then recursively or iteratively searching the 
appropriate half of the list.

 */


//// SOLUTION.

// Random Access is not allowed here means we can't turn it into an array. 
// One truth is that we need to find the length of the linked list. 
// And to do that, we need to transverse the linked list completely at least once which is O(n).
// I think i understand the 2 pointer thing. 
// If we use 2 pointers, a fast and a slow one, and we make the fast pointer move 2 steps and the slow pointer move one
// step, so  by the time the fast pointer is at the end, the slow pointer will most definitely be at the middle. 



function transverse(linkedList, target){


    function mainTransversal(list){
                    // Initialize both pointers to the starting variable. 
                    let head = list;
                    let prev = null; // This will point to the node before the middle
                    let slow = head;
                    let fast = head;
                    let value = slow.value

            // Traverse to find the middle
            while (fast !== null && fast.rest !== null) {
                prev = slow;
                slow = slow.rest;
                fast = fast.rest.rest;
                value = slow.value
            }

            // Now `prev` is the node before the middle, `slow` is the middle

            // Disconnect the two halves
            if (prev !== null) {
                prev.rest = null; // This separates the first half from the middle
            }

            // `head` is now the head of the first list (less than part)
            // `slow` is now the head of the second list (greater than or equal part)

            return [value,head,slow]
    }
            

            // Implement binary search. 

            let list2 = linkedList;
    while(list2.rest != null){
        let [mid, first, second] = mainTransversal(list2)
        if (mid == target){
            return true
        }else if (target > mid){
            list2 = second
        }else if (target < mid){
            list2 = first
        }
    }

    return false
    

}  

function arrayToList(arr, count = 0) {
  // Base case: if the current index is beyond the last element
  if (count >= arr.length) {
    // Return null to signify the end of the list
    return null;
  } else {
    // Create a node with the current element and a reference to the next node
    return {
      value: arr[count],
      rest: arrayToList(arr, count + 1),
    };
  }
}
// const eloquent = require('./eloquent') 

console.log(transverse(arrayToList([1,2,3,4,5,7]),8))
console.log(transverse(arrayToList([1,2,3,4,5,7]),5))