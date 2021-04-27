# Collision Handling for Hash Algorithms
This project contains python code for evaluating the performance of collision handling in hash maps. It implements Chaining, Linear Probing, Quadratic Probing and Double Hashing, with hash functions including Division, Multiplication and Prime.

## Usage
The main.py file holds everything needed to actually test data. 
* 1 - Create a hash map using either the OpenAddressing or Chaining class. (Specify the desired size (should match size of input data), hash function ("Division", "Multiplication" or "Prime) and desired probing method ("Linear", "Quadratic" or "Double") if using open addressing.
* 2 - Call the HashFunctions.hash_evaluation() function with a hash map, data set, item to delete (integer) and item to find (integer).
* 3 - You're all set! 

Your main.py (*or whatever you want to call it*) should look something like this:
```python
from OpenAddressing import OpenAddressing
import HashFunctions
import random

hash_map = OpenAddressing(150, "Division", "Linear")
item_to_delete = random.randrange(0,3000)
item_to_find = random.randrange(0,3000)
HashFunctions.hash_evaluation(hash_map, "datasetname.txt", item_to_delete, item_to_find)
```


## Included Data Sets
The included data sets are randomly generated lists with an integer key and a corresponding "firstname lastname" string value.
Any data set of this form should work, do bear in mind though, that the code *as is* cannot handle other than integer keys.
