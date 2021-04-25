import math

def get_hash(key, size, hashMode):
    """Hashes input key to an index in the hash map. size is the size of the hash map. hashMode can be either 'Division, Multiplication, Universal or Prime'"""
    if hashMode == "Division":
        h = 0
        for char in key:
            h += ord(char)
        h = h % size
        return h
    
    if hashMode == "Multiplication":
        h = 0
        for char in key:
            h += ord(char)
        h = math.floor(size * (h*0.6180339887 - math.floor(h*0.6180339887)))
        return h

    if hashMode == "Universal":
        h = 0
        for char in key:
            h += ord(char)
        return

    if hashMode == "Prime":
        h = 0
        for char in key:
            h += ord(char)
        h = (5 - (h % 5))
        return h