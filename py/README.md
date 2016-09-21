Author: Eli Cohen
Date: 09/21/2016


This folder contains three Python (2.7) scripts:

	1. basichash.py - the most basic implementation of a hash table in Python
	2. goodhash.py - an improved version of basichash, using popular techniques to improve runtime
	3. test.py - a script which tests the performance of each implementation, providing time metadata on the tests for comparison

To run the tests and evaluate the performance, simply unzip this folder, and inside the folder run:
	
	$ python test.py

Labeled results will print to the console, and you can examine the test script for information as to how the tests are run.

If you wish to test the implementation yourself, feel free to add "import goodhash.py" to any Python script and use its constructor, setter, getter, deleter, and load functions.


basichash.py - Stores values in an array, and when adding a key/value pair it looks sequentially for an empty spot starting from the beginning of the array; when getting a value or deleting a key/value pair, it looks sequentially from the beginning of the array for the correct key; it utilizes two separate arrays for keys and values to save memory; other implementations may use pointers to tuples for example.

goodhash.py - Also utilizes two arrays to store keys and values; when storing a key, it hashes the key to an integer and connects that to a corresponding bucket (if empty, it probes sequentially starting from that hashed index); when getting or deleting, it again hashes the key to find the target location, and again probes sequentially from that index to find the appropriate key (if it hits an empty bucket, it assumes the key was not set and returns None).

Features left out:
1. Quadratic probing - A collision resolution technique that involves probing for an empty bucket quadratically instead of linearly (e.g. i^n, as i increments with each collision). However, this could not be used with the built-in Python function "enumerate", which has significant performance savings over indexing to each new element as the index increments. Tests showed that enumerate was the better of the two choices.

2. Linked lists - The requirements limit the implementation to a fixed-size hash table, so this was not an option, but is a very popular implementation of basic hash tables.