/*
 Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first 
out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, 
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of 
that type). They cannot select which specific animal they would like. Create the data structures to 
maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog, 
and dequeueCat. 
 */

class Animal {
    constructor(name, type, order) {
        this.name = name;
        this.type = type.toLowerCase();
        this.order = order; // Tracks when the animal was enqueued
    }
}

class Shelter {
    constructor() {
        this.dogQueue = []; // Queue for dogs
        this.catQueue = []; // Queue for cats
        this.order = 0;     // Global counter for the order of all animals
    }

    // Enqueue either a dog or a cat
    enqueue(name, type) {
        let animal = new Animal(name, type, this.order);
        this.order++;  // Increment global order with each new animal

        if (animal.type === 'dog') {
            this.dogQueue.push(animal);
        } else if (animal.type === 'cat') {
            this.catQueue.push(animal);
        } else {
            throw new Error(`Invalid type. Expected 'dog' or 'cat', but got '${type}'`);
        }
    }

    // Dequeue the oldest dog
    dequeueDog() {
        if (this.dogQueue.length === 0) {
            return 'No dogs available';
        }
        return this.dogQueue.shift().name; // Remove and return the first dog
    }

    // Dequeue the oldest cat
    dequeueCat() {
        if (this.catQueue.length === 0) {
            return 'No cats available';
        }
        return this.catQueue.shift().name; // Remove and return the first cat
    }

    // Dequeue the oldest animal, either dog or cat
    dequeueAny() {
        if (this.dogQueue.length === 0 && this.catQueue.length === 0) {
            return 'No animals available';
        }
        if (this.dogQueue.length === 0) {
            return this.dequeueCat(); // No dogs, return the oldest cat
        }
        if (this.catQueue.length === 0) {
            return this.dequeueDog(); // No cats, return the oldest dog
        }

        // Compare the order of the oldest dog and the oldest cat
        let dog = this.dogQueue[0];
        let cat = this.catQueue[0];

        if (dog.order < cat.order) {
            return this.dequeueDog(); // Dequeue the oldest dog
        } else {
            return this.dequeueCat(); // Dequeue the oldest cat
        }
    }
}

// Testing the optimized Shelter class
let shelter = new Shelter();

shelter.enqueue('GSD', 'Dog'); 
shelter.enqueue('Rotweiler', 'Dog');
shelter.enqueue('Labrador', 'Dog');
shelter.enqueue('Tiger', 'Cat');
shelter.enqueue('African Cape Lion', 'Cat');
shelter.enqueue('Lion', 'Cat');

console.log(shelter.dequeueAny());  
console.log(shelter.dequeueDog());  
console.log(shelter.dequeueCat());  
console.log(shelter.dequeueAny());  
