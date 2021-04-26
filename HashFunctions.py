import math

def get_hash(key, size, hashMode):
    """Hashes input key to an index in the hash map. size is the size of the hash map. hashMode can be either 'Division, Multiplication or Prime'"""
    if hashMode == "Division":
        h = key % size
        return h
    
    if hashMode == "Multiplication":
        h = math.floor(size * (key*0.6180339887 - math.floor(key*0.6180339887)))
        return h

    if hashMode == "Prime":
        h = (5 - (key % 5))
        return h