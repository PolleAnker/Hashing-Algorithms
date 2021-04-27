from OpenAddressing import OpenAddressing
from Chaining import Chaining
import HashFunctions
import random

# Set up hash maps to be filled with data (with sizes corresponding to size of data set)
OpenHash = OpenAddressing(150, "Division", "Linear")
ChainHash = Chaining(150, "Division")

# Randomize which value to look for, for deletion and searching (can be non-existent in dataset)
item_to_delete = random.randrange(0,3000)
item_to_find = random.randrange(0,3000)
# Alternatively, known values can be used; 
#                        for dataset(150): 798, 2793, 1001, and 76
#                        for dataset(500): 1044, 916, 2869, and 57
#                        for dataset(3000): 962, 1753, 92, and 2805

print("Item to find is " + str(item_to_find) + " and item to delete is " + str(item_to_delete))

print("OPEN HASHING")
HashFunctions.hash_evaluation(OpenHash, "Data/dataset(150).txt", item_to_delete, item_to_find)
#HashFunctions.hash_evaluation(OpenHash, "Data/dataset(500).txt", item_to_delete, item_to_find)
#HashFunctions.hash_evaluation(OpenHash, "Data/dataset(3000).txt", item_to_delete, item_to_find)
print("CHAIN HASHING")
#HashFunctions.hash_evaluation(ChainHash, "Data/dataset(150).txt", item_to_delete, item_to_find)
#HashFunctions.hash_evaluation(ChainHash, "Data/dataset(500).txt", item_to_delete, item_to_find)
#HashFunctions.hash_evaluation(ChainHash, "Data/dataset(3000).txt", item_to_delete, item_to_find)