class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_head(self, x):
        if self.size == 0:
            self.head = self.tail = Node(x)
        else:
            dummy = self.head
            self.head = Node(x)
            self.head.next = dummy
            self.head.next.prev = self.head
        self.size += 1

    def insert_tail(self, x):
        if self.size == 0:
            self.head = self.tail = Node(x)
        else:
            dummy = self.tail
            self.tail = Node(x)
            self.tail.prev = dummy
            self.tail.prev.next = self.tail
        self.size += 1
    
    def insert_after(self, node, x):
        if self.tail == node:
            self.insert_tail(x)
        else:
            pointer = self.head
            while True:
                if pointer == node:
                    dummy = pointer.next
                    pointer.next = Node(x)
                    pointer.next.next = dummy
                    pointer.next.next.prev = pointer.next
                    pointer.next.prev = pointer
                    self.size += 1
                    break
                elif pointer == None:
                    print("Node not found")
                    break
                else:
                    pointer = pointer.next

    def delete_head(self):
        if self.size == 0:
            print("Linked list is empty.")
        elif self.size == 1:
            self.head = self.tail = None
            self.size = 0
        elif self.size == 2:
            self.head = self.tail
            self.head.next = None
            self.head.prev = None
            self.size = 1
        else:
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1

    def delete_after(self, node):
        if node == self.tail:
            print(f"{node} is the tail.")
        else:
            pointer = self.head
            while True:
                if pointer == node:
                    dummy = pointer.next.next
                    if dummy == None:
                        pointer.next = None
                        self.tail = pointer
                    else:
                        pointer.next = dummy
                        pointer.next.prev = pointer
                    self.size -= 1
                    break
                elif pointer == None:
                    print("Node not found")
                    break
                else:
                    pointer = pointer.next
        
    def find(self, x):
        # Counting head as the zeroth index
        index = 0
        pointer = self.head
        while True:
            if pointer == x:
                return index
            elif pointer == None:
                return None
            else:
                pointer = pointer.next
                index += 1
    
    def get_at(self, i):
        pointer = self.head
        if self.size == 0:
            print("Empty List")
        elif i < 0 or i > self.size - 1:
            print("IndexError")
        else:
            while True:
                if i == 0:
                    return pointer
                else:
                    i -= 1
                    pointer = pointer.next

    def reverse(self):
        reversed_list = LinkedList()
        pointer = self.tail
        while pointer != None:
            reversed_list.insert_head(pointer.value)
            pointer = pointer.prev
        return reversed_list

    def __len__(self):
        return self.size

    def to_array(self):
        pointer = self.head
        arr = [] #Strictly speaking should use a pre defined array class from the other file, but using list to make things quicker
        while pointer != None:
            arr.append(pointer)
            pointer = pointer.next
        return arr

    # bonus print dunder function

    def __str__(self):
        if self.size == 0:
            return ("Empty List")
        else:
            pointer = self.head
            string = ""
            string = string + str(pointer.value)
            while pointer != self.tail:
                string = string + " <-> "
                pointer = pointer.next
                string = string + str(pointer.value)
            return string

