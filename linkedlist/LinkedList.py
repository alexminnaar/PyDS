from linkedlist.ListNode import ListNode

# linked list implementation
class LinkedList:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        new_node = ListNode(value)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, check_value):
        check_node = self.head
        is_found = False

        while (check_node):
            if (check_node.value == check_value):
                is_found = True
                break
            else:
                check_node = check_node.next_node

        return is_found
