# Hash Table

# This hash table implementation uses a simple hash function that sums the ASCII values of the characters in the key. The `add`, `remove`, and `lookup` methods allow you to manage key-value pairs in the hash table. Note that in this implementation, each instance of `HashTable` does not share data, so adding data to one instance will not affect another instance.
class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key):
        return sum(ord(c) for c in key)

    def add(self, key, value):
        hash_key = self.hash(key)
        if hash_key not in self.collection:
            self.collection[hash_key] = {}
        self.collection[hash_key][key] = value

    def remove(self, key):
        hash_key = self.hash(key)
        if hash_key in self.collection and key in self.collection[hash_key]:
            del self.collection[hash_key][key]

    def lookup(self, key):
        hash_key = self.hash(key)
        if hash_key in self.collection and key in self.collection[hash_key]:
            return self.collection[hash_key][key]
        return None

print(HashTable().hash('golf')) # 424
HashTable().add('golf', 'sport') # {'golf': 'sport'}
HashTable().add('dear', 'friend') # {'golf': 'sport', 'dear': 'friend'}
HashTable().add('read', 'book') # {'golf': 'sport', 'dear': 'friend', 'read': 'book'}
print(HashTable().lookup('golf')) # None (because we are creating a new instance of HashTable, so the previous data is not stored)
print(HashTable().lookup('cfc')) # None (because we are creating a new instance of HashTable, so the previous data is not stored)