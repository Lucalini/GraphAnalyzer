class Queue:


    def __init__(self, capacity):
        #Creates an empty Queue with a capacity
        self.items = [None] * capacity
        self.capacity = capacity
        self.num_items = 0
        self.front = 0
        self.back = 0

    def is_empty(self):
        #Returns True if the Queue is empty, and False otherwise
        if self.num_items == 0:
            return True
        else:
            return False

    def is_full(self):
        #Returns True if the Queue is full, and False otherwise
        if self.num_items == self.capacity:
            return True
        else:
            return False


    def enqueue(self, item):
        #If Queue is not full, enqueues (adds) item to Queue
        #If Queue is full when enqueue is attempted, raises IndexError

        if self.is_full():
            raise IndexError

        if self.is_empty():
            self.items[self.front] = item
            self.num_items += 1
            self.back +=1
            return

        if self.back == (self.capacity - 1):
            self.items[self.back] = item
            self.num_items += 1
            self.back = 0
            return

        self.items[self.back] = item
        self.num_items +=1
        self.back +=1


    def dequeue(self):
        #If Queue is not empty, dequeues (removes) item from Queue and returns item.
        #If Queue is empty when dequeue is attempted, raises IndexError
        if self.is_empty():
            raise IndexError

        if self.front == (self.capacity -1):
            return_val = self.items[self.front]
            self.items[self.front] = None
            self.front = 0
            self.num_items -= 1
            return return_val

        return_val = self.items[self.front]
        self.items[self.front] = None
        self.front += 1
        self.num_items -= 1
        return return_val



    def size(self):
        return self.num_items


