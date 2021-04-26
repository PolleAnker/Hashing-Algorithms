from OpenAddressing import OpenAddressing
from Chaining import Chaining
import HashFunctions
import random

# Set up hash maps to be filled with data (with sizes corresponding to size of data set)
OpenHash = OpenAddressing(3000, "Division", "Linear")
ChainHash = Chaining(3000, "Division")

# Randomize which value to look for, for deletion and searching (can be non-existent in dataset)
item_to_delete = random.randrange(0,3000)
item_to_find = random.randrange(0,3000)
# Alternatively, known values can be used; 
#                        for dataset(150): 798, 2793, 1001, and 76
#                        for dataset(500): 1044, 916, 2869, and 57
#                        for dataset(3000): 962, 1753, 92, and 2805

print("Item to find is " + str(item_to_find) + " and item to delete is " + str(item_to_delete))

print("OPEN HASHING")
HashFunctions.hash_evaluation(OpenHash, "dataset(3000).txt", item_to_delete, item_to_find)
print("CHAIN HASHING")
HashFunctions.hash_evaluation(ChainHash, "dataset(3000).txt", item_to_delete, item_to_find)