import math
import time
import tracemalloc

def get_hash(key, size, hash_mode):
    """Hashes input key to an index in the hash map. size is the size of the hash map. hash_mode can be either 'Division, Multiplication or Prime'"""
    if hash_mode == "Division":
        hashed_key = key % size
        return hashed_key
    
    if hash_mode == "Multiplication":
        hashed_key = math.floor(size * (key*0.6180339887 - math.floor(key*0.6180339887)))
        return hashed_key

    if hash_mode == "Prime":
        hashed_key = (5 - (key % 5))
        return hashed_key


def hash_evaluation(hash_map, dataset, item_to_delete, item_to_find):
    start_time_in = time.time()
    tracemalloc.start()
    # Hashing dataset
    with open(dataset, "r") as set:
        for line in set:
            tokens = line.split(',')
            _id = int(tokens[0])
            try:
                name = tokens[1]
                hash_map[_id] = name
            except:
                print("Invalid entry, ignoring row")

    current_mem_in, peak_mem_in = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    executionTimeIn = time.time() - start_time_in
    # Delete metrics

    print("Item to delete is: " + str(hash_map[item_to_delete]))
    start_time_del = time.time()
    tracemalloc.start()
    del hash_map[item_to_delete]
    current_mem_del, peak_mem_del = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    execution_time_del = time.time() - start_time_del
    print("Item is now: " + str(hash_map[item_to_delete]))
    # Search metrics
    start_time_search = time.time()
    tracemalloc.start()
    print("Search result: " + hash_map[item_to_find])
    execution_time_search = time.time() - start_time_search
    current_mem_search, peak_mem_search = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("__________________________________________________________________________")
    print("PEAK MEMORY USAGE ON " + dataset)
    print("Peak memory usage for hashing items was: " + str(peak_mem_in / 10**6) + " MB")
    print("Peak memory usage for deleting item was: " + str(peak_mem_del / 10**6) + " MB")
    print("Peak memory usage for finding item was: " + str(peak_mem_search / 10**6) + " MB")
    print("__________________________________________________________________________")
    print("EXECUTION TIME FOR HASH FUNCTIONS ON " + dataset)
    print("Execution time of hashing items was: " + str(executionTimeIn) + " seconds")
    print("Execution time of deleting items was: " + str(execution_time_del) + " seconds")
    print("Execution time of finding items was: " + str(execution_time_search) + " seconds")
    print("__________________________________________________________________________")
