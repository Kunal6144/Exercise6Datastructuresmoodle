class HashTable:
    def __init__(self, size=256):
        self.size = size
        self.slots = [None] * size
        self.used_slots = 0  # Counter to keep track of used slots

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        hash_value = self._hash(key)
        index = hash_value
        while True:
            if self.slots[index] is None:
                self.slots[index] = {key: value}
                self.used_slots += 1
                break
            index = (index + 1) % self.size
            if index == hash_value:
                raise MemoryError("Hash table is full")

    def get(self, key, alternative=None):
        hash_value = self._hash(key)
        index = hash_value
        while True:
            if self.slots[index] is not None and key in self.slots[index]:
                return self.slots[index][key]
            index = (index + 1) % self.size
            if index == hash_value or self.slots[index] is None:
                return alternative


# Test the get() method
h = HashTable()
h.put('Name', 'HashTable')
print(h.get('Name'))  # Expected output: HashTable
