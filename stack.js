/**
 * Class representing a basic stack.
 */
class BasicStack {
    /**
     * Create a stack.
     */
    constructor() {
        /**
         * The container to hold the stack elements.
         * @type {Array}
         */
        this.container = [];
    }

    /**
     * Push an element onto the stack.
     * @param {*} element - The element to be added to the stack.
     */
    push(element) {
        this.container.push(element);
    }

    /**
     * Peek at the top element of the stack without removing it.
     * @returns {*} The top element of the stack.
     */
    peek() {
        return this.container[this.container.length - 1] || null;
    }

    /**
     * Pop and remove the top element from the stack.
     * @returns {*} The top element, or null if the stack is empty.
     */
    pop() {
        if (this.container.length === 0) {
            return null;
        }
        return this.container.pop();
    }

    /**
     * Check if the stack is empty.
     * @returns {boolean} True if the stack is empty, otherwise false.
     */
    isEmpty() {
        return this.container.length === 0;
    }

    /**
     * Get the size of the stack.
     * @returns {number} The number of elements in the stack.
     */
    get size() {
        return this.container.length;
    }
}

/**
 * Class representing three stacks implemented using a single array.
 */
class ThreeInOne {
    /**
     * Creates an instance of the ThreeInOne class.
     * The array has a fixed length of 15, divided equally into 3 stacks of 5 elements each.
     */
    constructor() {
        /**
         * The main array used to store elements for all three stacks.
         * @type {Array<null|*>}
         */
        this.array = new Array(15).fill(null);

        /**
         * Size of each stack.
         * @type {number}
         */
        this.size = 5;

        /**
         * An array to track the top pointer of each stack.
         * Initially, all stacks are empty, so top pointers are set to -1.
         * @type {Array<number>}
         */
        this.tops = [-1, -1, -1]; // Stack 1, Stack 2, Stack 3

        /**
         * Boundaries for each stack in the main array.
         * Stack 1 starts at index 0, Stack 2 at index 5, and Stack 3 at index 10.
         * @type {Array<number>}
         */
        this.boundaries = [0, 5, 10];
    }

    /**
     * Pushes a value onto the specified stack.
     * @param {number} stackNum - The stack number (0 for Stack 1, 1 for Stack 2, 2 for Stack 3).
     * @param {*} value - The value to push onto the stack.
     * @throws {Error} Will throw an error if the stack is full.
     */
    push(stackNum, value) {
        if (this.tops[stackNum] < this.size - 1) {
            this.tops[stackNum]++;
            const index = this.boundaries[stackNum] + this.tops[stackNum];
            this.array[index] = value;
        } else {
            throw new Error(`Stack ${stackNum + 1} is full!`);
        }
    }

    /**
     * Pops a value from the specified stack.
     * @param {number} stackNum - The stack number (0 for Stack 1, 1 for Stack 2, 2 for Stack 3).
     * @returns {*} The value that was popped from the stack.
     * @throws {Error} Will throw an error if the stack is empty.
     */
    pop(stackNum) {
        if (this.tops[stackNum] >= 0) {
            const index = this.boundaries[stackNum] + this.tops[stackNum];
            const value = this.array[index];
            this.array[index] = null;
            this.tops[stackNum]--;
            return value;
        } else {
            throw new Error(`Stack ${stackNum + 1} is empty!`);
        }
    }

    /**
     * Peeks at the top value of the specified stack without removing it.
     * @param {number} stackNum - The stack number (0 for Stack 1, 1 for Stack 2, 2 for Stack 3).
     * @returns {*} The value at the top of the stack.
     * @throws {Error} Will throw an error if the stack is empty.
     */
    peek(stackNum) {
        if (this.tops[stackNum] >= 0) {
            const index = this.boundaries[stackNum] + this.tops[stackNum];
            return this.array[index];
        } else {
            throw new Error(`Stack ${stackNum + 1} is empty!`);
        }
    }

    /**
     * Checks if the specified stack is empty.
     * @param {number} stackNum - The stack number (0 for Stack 1, 1 for Stack 2, 2 for Stack 3).
     * @returns {boolean} True if the stack is empty, false otherwise.
     */
    isEmpty(stackNum) {
        return this.tops[stackNum] === -1;
    }
}



let exampleStack = new BasicStack()
exampleStack.push(4)
exampleStack.push(5)
exampleStack.push(6)
exampleStack.push(7)

console.log(exampleStack.pop())
console.log(exampleStack.isEmpty())
console.log(exampleStack.size)

module.exports = {BasicStack, ThreeInOne}