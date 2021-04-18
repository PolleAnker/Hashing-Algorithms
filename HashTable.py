class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
        print('Created')

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        print(h % self.MAX)
        return h % self.MAX

    def add(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val