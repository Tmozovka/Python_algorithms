"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        pos = self.calculate_hash_value(string)
        if self.table[pos] is None :
            self.table[pos] = string
        elif type(self.table[pos]) is list:
            self.table[pos].append(string)
        else: 
            self.table[pos] = [self.table[pos], string]


    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        pos = self.calculate_hash_value(string)
        if self.table[pos] is not None:
            if self.table[pos] == string:
                return pos
            elif type(self.table[pos]) is list and string in self.table[pos]:
                return pos
        return -1    

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        return (ord(string[0]) * 100) + ord(string[1])
    
# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print (hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case
# Should be -1
print (hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')
# Should be 8568
print (hash_table.lookup('UDACITY'))

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print (hash_table.lookup('UDACIOUS'))
