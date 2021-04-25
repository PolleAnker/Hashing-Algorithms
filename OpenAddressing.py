"Linear Probing implementation"
import HashFunctions

class OpenAddressing:
    """Hash map using 'open addressing' to handle collisions. 
        It takes a desired hash function ('Division, Multiplication, Universal or Prime') 
        and desired probing method ('Linear, Quadratic or Double) as input"""
    def __init__(self, hashFunction, probeMode):
        self.hashFunction = hashFunction
        self.probeMode = probeMode
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    
    "MAIN FUNCTIONS (Set, Get and Delete items)"
    def __setitem__(self, key, val):
        "Set an item / index in hash map to be found with the key and hold the value val"
        if self.probeMode == "Double":
            h = HashFunctions.get_hash(key, self.MAX, "Division")
        else:
            h = HashFunctions.get_hash(key, self.MAX, self.hashFunction)
        
        if self.arr[h] is None:
            self.arr[h] = (key, val)
        else:
            new_h = self.find_open_slot(key, h)
            self.arr[new_h] = (key,val)

    def __getitem__(self, key):
        "Takes a key as input, which it finds in the hash map, returning its corresponding value."
        h = HashFunctions.get_hash(key, self.MAX, self.hashFunction)
        if self.arr[h] is None:
            return
        probingRange = self.get_probing_range(h)
        for probeIndex in probingRange:
            element = self.arr[probeIndex]
            if element is None:
                return
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        "Delete the given key and corresponding value from the hash map"
        h = HashFunctions.get_hash(key, self.MAX, self.hashFunction)
        probingRange = self.get_probing_range(h)
        for probeIndex in probingRange:
            if self.arr[probeIndex][0] == key:
                self.arr[probeIndex]= "Deleted"
                return
            if self.arr[probeIndex] is None:
                raise Exception("Element to delete not found")


    "HELPER FUNCTIONS (For assisting in finding new hash map indices in case of collision)"
    def get_probing_range(self, index):
        "Set probing range to be from the index (hashed key) to the length of the hashmap, and from the start to the index"
        return [*range(index, len(self.arr))] + [*range(0, index)]

    def find_open_slot(self, key, index):
        "Calculate a new hash map index in case of collision"
        probingRange = self.get_probing_range(index)
        for probeIndex in probingRange:
            
            if self.probeMode == "Linear":
                probeIndex = probeIndex
            if self.probeMode == "Quadratic":
                probeIndex = (index + (probeIndex**2)) % self.MAX
            if self.probeMode == "Double":
                h2 = HashFunctions.get_hash(key, self.MAX, "Prime")
                probeIndex = (index + (probeIndex * h2)) % self.MAX
            
            if self.arr[probeIndex] is None:
                return probeIndex
            if self.arr[probeIndex] == "Deleted":
                return probeIndex
            if self.arr[probeIndex][0] == key:
                return probeIndex
        raise Exception("Hashmap is full!")