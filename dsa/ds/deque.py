from LinkedList.py import LinkedList

class deque():

    def __init__(self, data):
        self.data = LinkedList()
    
    def enqueue(self, x):
        self.data.insert_tail(x)

    def dequeue(self):
        if self.data.size() == 0:
            return "Empty Queue"
        else:
            front = self.data.head
            self.data.delete_head()
            return front

    def peak_front(self):
        if self.data.size() == 0:
            return "Empty Queue"
        else:
            return self.data.head

    def peak_back(self):
        if self.data.size() == 0:
            return "Empty Queue"
        else:
            return self.data.tail

    def push_front(self, x):
        self.data.insert_head(x)

    def pop_back(self):
        if self.data.size() == 0:
            return "Empty Queue"
        else:
            back = self.data.tail
            self.data.delete_tail()
            return back

    def is_empty():
        retrun self.data.size == 0