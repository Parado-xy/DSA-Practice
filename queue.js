/**
 * A simple implementation of a queue using an array as the underlying container.
 */
class BasicQueue {
    /**
     * Initializes an empty queue.
     */
    constructor() {
        /**
         * The container to store the queue elements.
         * @type {Array<*>}
         */
        this.container = [];
    }

    /**
     * Adds an item to the end of the queue.
     * @param {*} item - The item to be added to the queue.
     */
    add(item) {
        this.container.push(item);
    }

    /**
     * Removes and returns the first item from the queue.
     * @returns {*} The item removed from the queue.
     */
    remove() {
        return this.container.shift(); // shift is more intuitive and achieves the same as splice(0,1)
    }

    /**
     * Returns the item at the front of the queue without removing it.
     * @returns {*} The first item in the queue.
     */
    peek() {
        return this.container[0];
    }

    /**
     * Checks whether the queue is empty.
     * @returns {boolean} True if the queue is empty, false otherwise.
     */
    isEmpty() {
        return this.container.length === 0;
    }
}
