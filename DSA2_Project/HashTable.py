'''
The HashTable class is a self-adjusting data structure which we will use to store our package information. It works
hand in hand with the Package class and has an insert function which we can use to populate package data from a
CSV file further on. I have opted to separate the HashTable from the Package class, preferring to keep the two
decoupled and modular in case I want to change the data structure at a later time.
'''


class HashTable:
    def __init__(self, capacity=40):
        self.table = []
        for i in range(capacity):
            self.table.append([])

    def __str__(self):
        return str(self.table)

    def insert(self, key, value):
        bucket = hash(key) % len(self.table)                                   # We take a hashed key, mod HashMap size,
        bucket_list = self.table[bucket]                                       # to find what bucket we'll use

        for pair in bucket_list:                                               # If this key is already present,
            if pair[0] == key:                                                 # we'll update the value
                pair[1] = value
                # TEST: print(f"Bucket {bucket} was updated with value {value}.")
                return True

        key_value = [key, value]                                  # Otherwise, we'll append the item to the bucket list
        bucket_list.append(key_value)
        # TEST: print(f"Value {value} was inserted into bucket {bucket}")
        return True

    # Search function requiring key argument
    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # For loop to search bucket
        for pair in bucket_list:
            if pair[0] == key:
                return pair[1]
                # Here, we return if found
        return None                                    # Return None if not found

    def remove(self, key):                             # While not required in the rubric, will be useful for our algorithm later
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for pair in bucket_list:                       # Iterate of bucket_list and remove pair if key is found
            if pair[0] == key:
                bucket_list.remove([pair[0], pair[1]])