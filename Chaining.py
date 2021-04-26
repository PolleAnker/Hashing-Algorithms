'Hash table using chaining to handle collisions'
import HashFunctions

class Chaining:
    def __init__(self, size ,hash_function):
        self.hash_function = hash_function
        self.MAX = size
        self.hash_map = [[] for i in range(self.MAX)]

    def __setitem__(self, key, val):
        #Set an item / index in hash map to be found with the key and hold the value val
        hash = HashFunctions.get_hash(key, self.MAX, self.hash_function)
        found_element = False
        #If a key already exists at an index, add it in linked list form
        for index, element in enumerate(self.hash_map[hash]):
            if len(element)==2 and element[0] == key:
                self.hash_map[hash][index] = (key, val)
                found_element = True
                break
        if not found_element:
            self.hash_map[hash].append((key, val))

    def __getitem__(self, key):
        #Takes a key as input, which it finds in the hash map, returning its corresponding value.
        hash = HashFunctions.get_hash(key, self.MAX, self.hash_function)
        #If the element[0] (the key is a match) return the value at element[0] (the value connected to the key)
        for element in self.hash_map[hash]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        #Delete the given key and corresponding value from the hash map
        hash = HashFunctions.get_hash(key, self.MAX, self.hash_function)
        #Find the appropiate element, if it matches the key, delete the index
        for index, element in enumerate(self.hash_map[hash]):
            if element[0] == key:
                del self.hash_map[hash][index]