class HashTableOpen:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]





    ''' Hashing Functions '''
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX