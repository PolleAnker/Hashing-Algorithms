from OpenAddressing import OpenAddressing
from Chaining import Chaining
import HashFunctions

# Set up hash maps to be filled with data (with sizes corresponding to size of data set)
OpenHash = OpenAddressing(150, "Division", "Linear")

ChainHash = Chaining(150, "Division")

print("OPEN HASHING")
HashFunctions.hash_evaluation(OpenHash, "dataset(150).txt")
print("CHAIN HASHING")
HashFunctions.hash_evaluation(ChainHash, "dataset(150).txt")