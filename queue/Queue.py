# Implementation of the Queue data structure.
# Queues are FIFO
class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue_array = [0] * max_size
        self.head = 0
        self.tail = 0

    def queue_empty(self):
        return True if (self.head == self.tail) else False

    def enqueue(self, x):
        #assert (self.head == self.tail + 1), "No more space in the queue"
        self.queue_array[self.tail] = x
        if (self.tail == self.max_size):
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self):
        #assert (self.is_empty() != False), "Queue is empty, cannot dequeue"
        x = self.queue_array[self.head]
        if (self.head == self.max_size):
            self.head = 0
        else:
            self.head += 1
        return x







