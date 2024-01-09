class Stack:

    def __init__(self, capacity):
        #Creates and empty stack with a capacity
        self.capacity = capacity
        self.items = [None]*capacity
        self.num_items = 0 

    def is_empty(self):
        #Returns True if the stack is empty, and False otherwise
        if self.num_items == 0:
            return True
        else:
            return False

    def is_full(self):
        #Returns True if the stack is full, and False otherwise
        if self.num_items < self.capacity:
            return False
        else:
            return True

    def push(self, item):
        #If stack is not full, pushes item on stack. 
        #If stack is full when push is attempted, raises IndexError
        if self.is_full() == True:
            raise IndexError
        else:
            self.items[self.num_items] = item
            self.num_items += 1

    def pop(self): 
        #If stack is not empty, pops item from stack and returns item.
        #If stack is empty when pop is attempted, raises IndexError
        if self.is_empty():
            raise IndexError
        else:
            return_val = self.items[self.num_items -1]
            self.items[self.num_items -1] = None
            self.num_items -= 1
            return return_val

    def peek(self):
        #If stack is not empty, returns next item to be popped (but does not pop the item)
        #If stack is empty, raises IndexError
        if self.is_empty():
            raise IndexError
        else:
            return self.items[self.num_items -1]

    def size(self):
        return self.num_items
