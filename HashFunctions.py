"File holding get_hash functions for hashing a key to an index in the hash map"

def get_hash(key, size, hashMode):
    """Hashes input key to an index in the hash map. size is the size of the hash map. hashMode can be either 'Division, Multiplication, Universal or Prime'"""
    if hashMode == "Division":
        h = 0
        for char in key:
            h += ord(char)
        return h % size
    
    if hashMode == "Multiplication":
        h = 0
        for char in key:
            h += ord(char)
        return

    if hashMode == "Universal":
        h = 0
        for char in key:
            h += ord(char)
        return

    if hashMode == "Prime":
        h = 0
        for char in key:
            h += ord(char)
        return 