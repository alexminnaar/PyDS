import unittest

from stack.Stack import Stack


class StackTest(unittest.TestCase):
    def test_empty(self):
        empty_stack = Stack(5)
        is_empty = empty_stack.stack_empty()
        self.assertEqual(is_empty, True, "should be true")

    def test_push(self):
        my_stack = Stack(5)
        my_stack.push(2)
        my_stack.push(3)
        self.assertEqual(my_stack.stack_array, [2, 3, 0, 0, 0], "should be 2,3,0,0,0")


    def test_pop(self):
        my_stack = Stack(5)
        my_stack.push(2)
        my_stack.push(3)
        x = my_stack.pop()
        self.assertEqual(x, 3, "should be 3")
        self.assertEqual(my_stack.top, 0, "should be 0")


if __name__ == '__main__':
    unittest.main()