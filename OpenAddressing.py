"Linear Probing implementation"
import HashFunctions

class OpenAddressing:
    def __init__(self, hashFunction, probeMode):
        self.hashFunction = hashFunction
        self.probeMode = probeMode
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def __setitem__(self, key, val):
        'Set the given index, h, to be the key,val pair. Handle collision by checking if it is already occupied'
        h = HashFunctions.get_hash(key, self.MAX, self.hashFunction)
        if self.arr[h] is None:
            self.arr[h] = (key, val)
        else:
            new_h = self.find_open_slot(key, h)
            self.arr[new_h] = (key,val)

    def __getitem__(self, key):
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
        h = HashFunctions.get_hash(key, self.MAX, self.hashFunction)
        probingRange = self.get_probing_range(h)
        for probeIndex in probingRange:
            if self.arr[probeIndex][0] == key:
                self.arr[probeIndex]= "Deleted"
                return
            if self.arr[probeIndex] is None:
                raise Exception("Element to delete not found")

    def get_probing_range(self, index):
        'Set probing range to be from the index (hashed key) to the length of the hashmap, and from the start to the index'
        return [*range(index, len(self.arr))] + [*range(0, index)]

    def find_open_slot(self, key, index):
        'Calculate the new hash using the step, probeIndex as the new hashed value'
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