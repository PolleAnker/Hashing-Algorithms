from OpenAddressing import OpenAddressing
from Chaining import Chaining


# Set up hash maps to be filled with data (with sizes corresponding to size of data set)
OpenHash_150 = OpenAddressing(150, "Division", "Linear")
OpenHash_500 = OpenAddressing(500, "Division", "Linear")
OpenHash_3000 = OpenAddressing(3000, "Division", "Linear")

Chaining_150 = Chaining(150, "Division")
Chaining_500 = Chaining(500, "Division")
Chaining_3000 = Chaining(3000, "Division")


# Open file and hash the contents to the selected hashmap
with open("dataset(150).txt", "r") as f:
    for line in f:
        tokens = line.split(',')
        _id = int(tokens[0])
        try:
            name = tokens[1]
            OpenHash_150[_id] = name
            Chaining_150[_id] = name
        except:
            print("Invalid entry, ignoring row")

print("OPEN ADDRESSING METHOD")
print(OpenHash_150.arr)
print("__________________________________________________________________________")
print("CHAINING METHOD")
print(Chaining_150.arr)