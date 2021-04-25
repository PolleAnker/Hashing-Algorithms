from Chaining import Chaining
from OpenAddressing import OpenAddressing

HTC = Chaining()
HOA = OpenAddressing()

HOA["march 6"] = 130
HOA["march 17"] = 20
valHOA = HOA["march 6"]
valHOA2 = HOA["march 17"]
valHOANull = HOA["march 20"]
print(valHOA)
print(valHOA2)
print(valHOANull)
print(HOA.arr)

