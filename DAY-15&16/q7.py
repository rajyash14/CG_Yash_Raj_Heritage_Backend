#Hash Table Implementation (Separate Chaining)

class ChainHashTable:
    def __init__(self, size=8):
        self.size    = size
        self.buckets = [[] for _ in range(size)]
        
    def _hash(self, key):
        return hash(key) % self.size
        
    def put(self, key, value):
        idx    = self._hash(key)
        bucket = self.buckets[idx]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        
    def get(self, key):
        bucket = self.buckets[self._hash(key)]
        for k, v in bucket:
            if k == key: return v
        return None
        
    def display(self):
        for i, bucket in enumerate(self.buckets):
            if bucket:
                print(f'Slot {i}: {bucket}')

ht = ChainHashTable(size=4)
words = ['cat', 'dog', 'rat', 'ant', 'bee', 'emu']
for w in words:
    ht.put(w, w.upper())
    
ht.display()