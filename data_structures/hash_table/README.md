# Hashtable
Implementation of Hash Table

## API

### Initialization
HashTable(*[max_size]*)
Optional max_size is type <int>, is 1024 by default and defines the number of buckets used by the hash table. If a non-negative integer is specified, the hashtable will use more memory but provide faster access.

### .set(*key, value*)
insert key:value pair into hash table
key must be type <str>

### .get(*key*)
retrieve *value* stored at *key*
key must be type <str>

### .remove(*key [, emptybuc]*)
retrieves *value* stored at *key* and removes key:value pair from hash table
Optional emptybuc is type <bool> and is False by default. If True, all key:value pairs where the key hashes to the same hash as *key* will be removed from the hash table
