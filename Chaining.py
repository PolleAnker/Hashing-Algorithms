'Hash table using chaining to handle collisions'
import HashFunctions

class Chaining:
    def __init__(self, hashFunction):
        self.hashFunction = hashFunction
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def __setitem__(self, key, val):
        h = HashFunctions.get_hash(key, self.MAX, self.hashFunction)
        foundelement = False
        'If a key already exists at an index, add it in linked list form (Chaining approach)'
        for index, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:
                self.arr[h][index] = (key, val)
                foundelement = True
                break
        if not foundelement:
            self.arr[h].append((key, val))

    def __getitem__(self, key):
        h = HashFunctions.get_hash(key, self.MAX, self.hashFunction)
        'If the element[0] (the key is a match) return the value at element[0] (the value connected to the key)'
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = HashFunctions.get_hash(key, self.MAX, self.hashFunction)
        'Find the appropiate element, if it matches the key, delete the index'
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]