from Chaining import Chaining
from OpenAddressing import OpenAddressing

HTC = Chaining()
HOA = OpenAddressing()


HTC["march 6"] = 130
HTC["march 17"] = 20
valHTC = HTC["march 6"]
print(valHTC)
print(HTC.arr)


HOA["march 6"] = 130
HOA["march 17"] = 20
valHOA2 = HOA["march 17"]
valHOA = HOA["march 6"]
valHOANull = HOA["march 20"]
print(valHOA)
print(valHOA2)
print(valHOANull)
print(HOA.arr)