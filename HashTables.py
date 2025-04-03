class HashTable:
    def __init__(self, size=10):
        # Initialize the hash table with empty buckets
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        # Simple hash function: sum of character codes modulo table size
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, value):
        # Compute the hash index
        index = self._hash_function(key)
        # Check if the key already exists and update it
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        # Otherwise, add the new key-value pair
        self.table[index].append([key, value])

    def get(self, key):
        # Compute the hash index
        index = self._hash_function(key)
        # Search for the key in the bucket
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        # Key not found
        return None

    def delete(self, key):
        # Compute the hash index
        index = self._hash_function(key)
        # Search for the key in the bucket and remove it
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                return True
        # Key not found
        return False

    def display(self):
        # Print the hash table for visualization
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")

# Example usage
if __name__ == "__main__":
    ht = HashTable(size=5)
    ht.insert("apple", 1)
    ht.insert("banana", 2)
    ht.insert("orange", 3)
    ht.insert("grape", 4)
    ht.insert("kiwi", 5)

    ht.display()

    print("Get 'banana':", ht.get("banana"))
    print("Delete 'orange':", ht.delete("orange"))
    ht.display()
    print("Get 'orange':", ht.get("orange"))
    print("Delete 'banana':", ht.delete("banana"))
    ht.display()
    print("Get 'banana':", ht.get("banana"))
    print("Delete 'banana':", ht.delete("banana"))
    ht.display()
    