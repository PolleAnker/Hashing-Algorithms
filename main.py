from Chaining import Chaining
from OpenAddressing import OpenAddressing

"Open Addressing Test"
HOA = OpenAddressing("Division", "Linear")

HOA["march 6"] = 130
HOA["march 17"] = 20
HOA["march 26"] = 58
HOA["march 08"] = 70
valHOA = HOA["march 6"]
valHOA2 = HOA["march 17"]
valHOANull = HOA["march 20"]
valHOA3 = HOA["march 26"]
print(valHOA)
print(valHOA2)
print(valHOANull)
print(valHOA3)
print(HOA.arr)

del HOA["march 17"]
print(HOA.arr)
HOA["march 17"] = 20 
print(HOA.arr)

"""
"Chaining Test"
HTC = Chaining()

HTC["march 6"] = 130
HTC["march 17"] = 20
valHTC = HTC["march 6"]
valHTC2 = HTC["march 17"]
valHTCNull = HTC["march 20"]
print(valHTC)
print(valHTC2)
print(valHTCNull)
print(HTC.arr)
del HTC["march 17"]
print(HTC.arr)
"""
