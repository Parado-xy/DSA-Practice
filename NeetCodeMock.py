# Question: Create a class that stores integer values.
# There should be non-duplicates. 
# a remove method for removing a value from the index. 
# a get_random method that returns a random value.

import random 

class Store: 
    def __init__(self):
        self.map = {}
        self.list = []

    def insert(self, value):
        if value not in self.map:
            self.list.append(value)
            self.map[value] = len(self.list) - 1
            return True 
        return False 

    def remove(self, value):
        if value in self.map: 
            # Get index of value from map. 
            index = self.map[value]
            # get the  last value of the list. 
            last_value = self.list[len(self.list) - 1]
            # Swap out last for the element at `index` 
            self.list[len(self.list) - 1 ], self.list[index] = value, last_value 
            # Update the index of the last_value
            self.map[last_value] = index
            # Remove the `value` which is now the last element from the list
            self.list.pop()
            del self.map[value]
            return True 
        return False 
    
    def get_random(self):

        if not self.list:
            return None

        choice_count = len(self.list) - 1
        random_index = random.randint(0, choice_count)

        return  self.list[random_index]
