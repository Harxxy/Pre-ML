def hash_string(s):
    h = 0

    for c in s:
        h = (h * 31 + ord(c)) % (2**16)

    return h

class Pair:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"({self.key} : {self.value})"

class HashmapLP:

    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.data = [None] * self.capacity
        self.hash_data = [None] * self.capacity

    @property
    def load(self):
        return self.size / self.capacity

    def resize(self, factor):
        arr = [None] * self.capacity
        for i in range(self.capacity):
            if self.data[i] != None:
                arr[i] = self.data[i]
        self.capacity = max(4, int(self.capacity * factor))
        self.data = [None] * self.capacity
        self.hash_data = [None] * self.capacity
        for element in arr:
            if element is None:
                continue
            i = hash_string(element.key) % self.capacity
            while True:
                if self.data[i] is None:
                    self.data[i] = Pair(element.key, element.value)
                    self.hash_data[i] = hash_string(element.key) % self.capacity                                          
                    break
                else: #No need to check for if the loop iterates back to original i since in my implementation the hashmap can never be full
                    i = (i + 1) % self.capacity

    def put(self, k, v):
        i = hash_string(k) % self.capacity
        while True:
            if self.data[i] is None:
                self.data[i] = Pair(k, v)
                self.hash_data[i] = hash_string(k) % self.capacity
                self.size += 1
                if self.load > 0.5:
                    self.resize(2)                                         
                break
            elif self.data[i].key == k:
                self.data[i].value = v
                break
            else: #No need to check for if the loop iterates back to original i since in my implementation the hashmap can never be full
                i = (i + 1) % self.capacity
    
    def get(self, k):
        i = hash_string(k) % self.capacity
        while True:
            if self.data[i] is None:
                raise IndexError("Key not found")
            elif self.data[i].key == k:
                return self.data[i].value            
            else: #No need to check for if the loop iterates back to original i since in my implementation the hashmap can never be full
                i = (i + 1) % self.capacity

    def remove(self, k):
        i = hash_string(k) % self.capacity
        while True:
            if self.data[i] is None:
                raise IndexError("Key not found")
            elif self.data[i].key == k:
                self.data[i] = None
                self.hash_data[i] = None
                self.size -= 1
                break
            else: #No need to check for if the loop iterates back to original i since in my implementation the hashmap can never be full
                i = (i + 1) % self.capacity
        traversed = 0
        while True:
            i = (i + 1) % self.capacity
            traversed += 1
            if self.data[i] is None:
                break
            elif ((i - self.hash_data[i]) % self.capacity) >= traversed:
                deleted_index = (i - traversed) % self.capacity
                self.data[deleted_index] = self.data[i]
                self.data[i] = None
                self.hash_data[deleted_index] = self.hash_data[i]
                self.hash_data[i] = None
                traversed = 0
            else:
                pass
        if self.load < 0.25:
            self.resize(0.5)
    
    def contains(self, k):
        i = hash_string(k) % self.capacity
        while True:
            if self.data[i] is None:
                return False
            elif self.data[i].key == k:
                return True
            else: #No need to check for if the loop iterates back to original i since in my implementation the hashmap can never be full
                i = (i + 1) % self.capacity  

