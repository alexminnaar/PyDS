import unittest

from queue.Queue import Queue


class QueueTest(unittest.TestCase):
    def test_empty(self):
        test_queue = Queue(5)
        is_empty = test_queue.queue_empty()
        self.assertEqual(is_empty, True, "should be true")

    def test_enqueue(self):
        test_queue = Queue(5)
        test_queue.enqueue(2)
        test_queue.enqueue(3)
        self.assertEqual(test_queue.head, 0, "head should be 0")
        self.assertEqual(test_queue.tail, 2, "tail should be 2")

    def test_dequeue(self):
        test_queue = Queue(5)
        test_queue.enqueue(2)
        test_queue.enqueue(3)
        x = test_queue.dequeue()
        y = test_queue.dequeue()
        self.assertEqual(x, 2, "2 should be dequeued first")
        self.assertEqual(y, 3, "3 should be dequeued second")


if __name__ == '__main__':
    unittest.main()