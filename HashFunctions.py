"Hash function, to be called in the collision handling scripts as get_hash"

def get_hash(key, size, hashMode):
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