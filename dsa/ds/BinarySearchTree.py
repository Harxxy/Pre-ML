class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return f"{{{self.key} : {self.value}}}"

class BinarySearchTree:

    def __init__(self, root=None):
        self.root = root

    def contains(self, x):
        pointer = self.root
        while True:
            if pointer is None:
                return False
            else:
                if pointer.key == x:
                    return True
                elif x < pointer.key:
                    pointer = pointer.left
                elif x > pointer.key:
                    pointer = pointer.right

    def search(self, k):
        pointer = self.root
        while True:
            if pointer is None:
                return None
            else:
                if pointer.key == k:
                    return pointer
                elif k < pointer.key:
                    pointer = pointer.left
                elif k > pointer.key:
                    pointer = pointer.right 

    def insert(self, k, v):
        pointer = self.root
        while True:
            if self.root is None:
                self.root = Node(k, v)
                return
            elif pointer.key == k:
                pointer.value = v
                break
            elif k < pointer.key:
                if pointer.left is None:
                    pointer.left = Node(k, v)
                    pointer.left.parent = pointer
                else:
                    pointer = pointer.left
            elif k > pointer.key:
                if pointer.right is None:
                    pointer.right = Node(k, v)
                    pointer.right.parent = pointer
                else:
                    pointer = pointer.right

    @property
    def minimum(self):
        if self.root is None:
            return None
        else:
            pointer = self.root
            while pointer.left is not None:
                pointer = pointer.left
            return pointer

    @property
    def maximum(self):
        if self.root is None:
            return None
        else:
            pointer = self.root
            while pointer.right is not None:
                pointer = pointer.right
            return pointer

    def successor(self, x):
        pointer = self.search(x)
        if pointer is None:
            return "No such key exists"
        if pointer.right is None:
            while True:
                back_pointer = pointer.parent 
                if back_pointer is None:
                    return f"Successor does not exist as {x} is the maximum" # That means x is the maximum in the tree
                elif back_pointer.left == pointer:
                    return back_pointer
                else:
                    pointer = back_pointer
        else:
            branch = BinarySearchTree(pointer.right)
            return branch.minimum

    def predecessor(self, x):
        pointer = self.search(x)
        if pointer is None:
            return "No such key exists"
        else:
            if pointer.left is None:
                while True:
                    back_pointer = pointer.parent 
                    if back_pointer is None:
                        return f"Successor does not exist as {x} is the minimum" # That means x is the minimum in the tree
                    elif back_pointer.right == pointer:
                        return back_pointer
                    else:
                        pointer = back_pointer
            else:
                branch = BinarySearchTree(pointer.left)
                return branch.maximum

    def traverse_range(self, lo, hi):
        if lo > hi:
            return "Minimum provided is greater than maximum provided"
        if self.contains(hi):
            journey = []
            pointer = self.search(lo)
            if pointer is None:
                return "Input minimum value does not exist"
            else:
                journey.append(pointer)
            while True:
                if pointer.right is None:
                    while True:
                        back_pointer = pointer.parent 
                        if back_pointer is None:
                            return journey # Back pointer never hits this case unless hi is max
                        elif back_pointer.left == pointer:
                            pointer = back_pointer
                            journey.append(pointer)
                            if pointer.key == hi:
                                return journey
                            break
                        else:
                            pointer = back_pointer
                else:
                    branch = BinarySearchTree(pointer.right)
                    pointer = branch.minimum
                    journey.append(pointer)
                    if pointer.key == hi:
                        return journey
        else:
            return "Input maximum value does not exist"


    def traverse_in_order(self): #Could just use the old function, but this one saves time by not having to calculate maximum (slightly faster)
        journey = []
        pointer = self.minimum
        if pointer is None:
            return "Empty BST"
        else:
            journey.append(pointer)
        while True:
            if pointer.right is None:
                while True:
                    back_pointer = pointer.parent 
                    if back_pointer is None:
                        return journey # We have reached the last element
                    elif back_pointer.left == pointer:
                        pointer = back_pointer
                        journey.append(pointer)
                        break
                    else:
                        pointer = back_pointer
            else:
                branch = BinarySearchTree(pointer.right)
                pointer = branch.minimum
                journey.append(pointer) #Binary traversal never ends in this branch, always ends under the if statement
              