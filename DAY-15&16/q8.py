#Hash Table Implementation (Open Addressing)

class OpenAddressHashTable:
    DELETED = object()
    
    def __init__(self, size=8):
        self.size    = size
        self.slots   = [None] * size
        self.count   = 0
        
    def _hash(self, key):  
        return hash(key) % self.size
        
    def put(self, key, value):
        if self.count / self.size > 0.7:
            self._resize()
            
        idx = self._hash(key)
        while self.slots[idx] is not None and self.slots[idx] is not self.DELETED:
            k, v = self.slots[idx]
            if k == key:
                self.slots[idx] = (key, value)
                return
            idx = (idx + 1) % self.size
            
        self.slots[idx] = (key, value)
        self.count += 1
        
    def get(self, key):
        idx = self._hash(key)
        while self.slots[idx] is not None:
            if self.slots[idx] is not self.DELETED:
                k, v = self.slots[idx]
                if k == key: return v
            idx = (idx + 1) % self.size
        return None
        
    def _resize(self):
        old = [s for s in self.slots if s and s is not self.DELETED]
        self.size *= 2
        self.slots = [None] * self.size
        self.count = 0
        for k, v in old: self.put(k, v)
        
    def display(self):
        for i, s in enumerate(self.slots):
            status = s if s else 'EMPTY'
            print(f'  [{i:2d}] {status}')

ht = OpenAddressHashTable(size=8)
for k, v in [('a',1),('b',2),('c',3),('d',4)]:
    ht.put(k, v)
ht.display()