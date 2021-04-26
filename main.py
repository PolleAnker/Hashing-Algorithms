from OpenAddressing import OpenAddressing
from Chaining import Chaining



# Set up hash maps to be filled with data (with sizes corresponding to size of data set)
OpenHash_150 = OpenAddressing(150, "Division", "Linear")
OpenHash_500 = OpenAddressing(500, "Division", "Linear")
OpenHash_3000 = OpenAddressing(3000, "Division", "Linear")

Chaining_150 = Chaining(150, "Division")
Chaining_500 = Chaining(500, "Division")
Chaining_3000 = Chaining(3000, "Division")


with open("dataset_150.csv", "r") as f:
    for line in f:
        tokens = line.split(',')
        _id = tokens[0]
        try:
            name = tokens[1]
            OpenHash_150[_id] = name
        except:
            print("Invalid name, ignore the row")

val_382 = OpenHash_150[382]
print(OpenHash_150.arr)
print(val_382)