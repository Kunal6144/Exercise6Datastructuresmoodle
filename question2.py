class HashTable:
    def __init__(self, size=256):
        self.size = size
        self.slots = [None] * size
        self.used_slots = 0  # Counter to keep track of used slots

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        # Calculate the hash value for the key
        hash_value = self._hash(key)

        # Check if the slot is empty
        if self.slots[hash_value] is None:
            # Add the key-value pair to the empty slot
            self.slots[hash_value] = {key: value}
            self.used_slots += 1
        else:
            # Collision: handle collision by linear probing
            index = hash_value
            while True:
                # Check if the key already exists in the slot
                if key in self.slots[index]:
                    # Update the value for the existing key
                    self.slots[index][key] = value
                    break

                # Move to the next slot (circularly)
                index = (index + 1) % self.size

                # Check if we have checked all slots
                if index == hash_value:
                    # If we have checked all slots without finding an empty slot, raise MemoryError
                    raise MemoryError("Hash table is full")

                # Check if the slot is empty
                if self.slots[index] is None:
                    # Add the key-value pair to the empty slot
                    self.slots[index] = {key: value}
                    self.used_slots += 1
                    break


# Test the put() method
h = HashTable()
h.put("Name", "HashTable")
print(h.slots[229])  # Expected output: {Name: HashTable}
