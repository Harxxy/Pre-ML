import ctypes

class DynamicArray:

    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.data = (ctypes.py_object * self.capacity)()

    def is_empty(self):
        return self.size == 0

    def resize(self, factor):
        self.capacity = max(int(self.capacity * factor), 1, self.size)
        arr, self.data = self.data, (ctypes.py_object * self.capacity)()
        for i in range(0, self.size):
            self.data[i] =  arr[i]

    def get(self, i):
        if self.is_empty():
            print("Empty Array")
        elif i < 0 or i >= self.size:
            print("IndexError")
        else:
            return self.data[i]

    def set_value(self, i, x):
        if i < 0 or i >= self.size:
            print("IndexError")
        else:
            self.data[i] = x

    def push_back(self, x):
        if self.size == self.capacity:
            self.resize(2)
        self.data[self.size] = x  
        self.size += 1

    def pop_back(self):
        if self.is_empty():
            print("Empty Array")
        else:
            x = self.data[self.size - 1]
            self.data[self.size - 1] = None
            self.size -= 1
            if self.size < self.capacity/4:
                self.resize(0.5)
            return x

    def insert_at(self, i, x):
        if self.is_empty() and i == 0:
            self.push_back(x)
        elif i < 0 or i > self.size:
            print("IndexError")
        else:
            if self.size == self.capacity:
                self.resize(2)
            for n in range(self.size, i, -1):
                self.data[n] = self.data[n-1]
            self.data[i] = x
            self.size += 1
    
    def remove_at(self, i):
        if self.is_empty():
            print("Empty Array")
        elif i < 0 or i >= self.size:
            print("IndexError")
        else:
            x = self.data[i]
            self.size -= 1
            for n in range(i, self.size):
                self.data[n] = self.data[n+1]
            self.data[self.size] = None
            if self.size < self.capacity/4:
                self.resize(0.5)
            return x
            
    def find(self, x):
        if self.is_empty():
            print("Empty Array")
        else:
            for i in range(0, self.size):
                if self.data[i] == x:
                    return i
            return -1
    