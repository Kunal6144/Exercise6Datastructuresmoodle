class HashTable:
    def __init__(self, size=26):
        self.size = size
        self.slots = [None] * size

    def _find_free_slot(self, position):
        # Start searching from the given position
        index = position
        while True:
            # Check if the current slot is empty
            if self.slots[index] is None:
                return index  # Found a free slot

            # Move to the next slot
            index = (index + 1) % self.size

            # If we reach the starting position again, return None
            if index == position:
                return None


# Test the _find_free_slot() method
h = HashTable()

# Fill some slots with values
for c in "abcdefghijklmnopqrstuvwxyz":
    h.slots[(ord(c) * ord(c)) % h.size] = c

# Test the method with different positions
print(h._find_free_slot(0))   # Expected output: 1
print(h._find_free_slot(1))   # Expected output: 2
print(h._find_free_slot(10))  # Expected output: 11
