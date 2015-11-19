# Implementation of a stack data structure.
# Stacks are FILO
class Stack:

    def __init__(self, max_size):
        self.max_size = max_size
        self.stack_array = [0] * max_size
        self.top = -1

    def stack_empty(self):
        return True if (self.top == -1) else False

    def push(self, x):
        assert (self.top + 1 <= self.max_size), "Stack Overflow!!!"

        self.top = self.top + 1
        self.stack_array[self.top] = x

    def pop(self):
        assert (self.stack_empty() != True), "Stack Underflow!!!"

        self.top = self.top - 1
        return self.stack_array[self.top + 1]
