from LinkedList import LinkedList

class Deque():

    def __init__(self):
        self.data = LinkedList()
    
    def enqueue(self, x):
        self.data.insert_tail(x)

    def dequeue(self):
        if self.data.size() == 0:
            raise IndexError("dequeue from empty queue")
        front = self.data.head.value
        self.data.delete_head()
        return front

    def peek_front(self):
        if self.data.size() == 0:
            raise IndexError("peek from empty queue")
        return self.data.head.value

    def peek_back(self):
        if self.data.size() == 0:
            raise IndexError("peek from empty queue")
        return self.data.tail.value

    def push_front(self, x):
        self.data.insert_head(x)

    def pop_back(self):
        if self.data.size() == 0:
            raise IndexError("pop from empty queue")
        back = self.data.tail.value
        self.data.delete_tail()
        return back

    def is_empty(self):
        return self.data.size() == 0