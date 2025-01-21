'''Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

 '''
import random
 
class RandomizedSet:

    def __init__(self):
        self.value_to_index={}
        self.values=[]

    def insert(self, val: int) -> bool:
        if val in self.value_to_index:
            return False
        
        self.values.append(val)
        self.value_to_index[val]=len(self.values)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.value_to_index:
            return False

        index = self.value_to_index[val]
        last_val = self.values[-1]

        self.values[index] = last_val
        self.value_to_index[last_val] = index

        self.values.pop()
        del self.value_to_index[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()