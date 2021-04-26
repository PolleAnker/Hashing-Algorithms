from OpenAddressing import OpenAddressing
from Chaining import Chaining
import HashFunctions

# Set up hash maps to be filled with data (with sizes corresponding to size of data set)
OpenHash = OpenAddressing(500, "Division", "Linear")

ChainHash = Chaining(500, "Division")

print("OPEN HASHING")
HashFunctions.hash_evaluation(OpenHash, "dataset(500).txt", 2784, 1450)
print("CHAIN HASHING")
HashFunctions.hash_evaluation(ChainHash, "dataset(500).txt", 2784, 1450)