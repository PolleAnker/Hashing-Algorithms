class OpenAddressing:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def __setitem__(self, key, val):
        'Set the given index, h, to be the key,val pair. Handle collision by checking if it is already occupied'
        i = 0
        h = self.get_hash(key)
        while not self.arr[h] is None:
            h = (h+i) % len(self.arr)
            i+=1
        self.arr[h] = val

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None




    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX