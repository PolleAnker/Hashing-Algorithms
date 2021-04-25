class OpenAddressing:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def __setitem__(self, key, val):
        'Set the given index, h, to be the key,val pair. Handle collision by checking if it is already occupied'
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key, val)
        else:
            new_h = self.find_open_slot(key, h)
            self.arr[new_h] = (key,val)
        print(self.arr)

    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return
        probingRange = self.get_probing_range(h)
        for probeIndex in probingRange:
            element = self.arr[probeIndex]
            if element is None:
                return
            if element[0] == key:
                return element[1]

    "Delete function is buggy and not working, not sure why"
    def __delitem__(self, key):
        amountOfFor = 0
        h = self.get_hash(key)
        probingRange = self.get_probing_range(h)
        for probeIndex in probingRange:
            amountOfFor += 1
            if self.arr[probeIndex] is None:
                print("Delete Item for loop was run " + str(amountOfFor) + " times")
                return # item not found so return. You can also throw exception
            if self.arr[probeIndex][0] == key:
                self.arr[probeIndex]=None
        print(self.arr)

    def get_probing_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0, index)]

    def find_open_slot(self, key, index):
        probingRange = self.get_probing_range(index)
        for probeIndex in probingRange:
            if self.arr[probeIndex] is None:
                return probeIndex
            if self.arr[probeIndex][0] == key:
                return probeIndex
        raise Exception("Hashmap is full!")


    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX