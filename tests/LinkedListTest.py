import unittest

from linkedlist.LinkedList import LinkedList
from linkedlist.ListNode import ListNode


class LinkedListTest(unittest.TestCase):
    def test_initialization(self):
        test_list = LinkedList(ListNode(3))
        self.assertEqual(test_list.head.value, 3, "head value should be 3")
        self.assertEqual(test_list.head.next_node, None, "head next node should be None")


    def test_insert(self):
        test_list = LinkedList(ListNode(3))
        self.assertEqual(test_list.head.value, 3, "head value should be 3")
        test_list.insert(2)
        self.assertEqual(test_list.head.value, 2, "new head value should be 2")


    def test_search(self):
        test_list = LinkedList(ListNode(3))
        test_list.insert(2)
        test_list.insert(5)
        self.assertEqual(test_list.search(3), True, "3 is in this list")


if __name__ == '__main__':
    unittest.main()