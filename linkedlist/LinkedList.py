from linkedlist.ListNode import ListNode

# linked list implementation
class LinkedList:
    def __init__(self, head):
        self.head = head

    def prepend(self, value):
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

    def insert(self, value, index):

        insert_node = ListNode(value)

        current_index = 0
        current_node = self.head

        while (current_index < index - 1):
            current_index += 1
            current_node = current_node.next_node
            print current_node.value

        insert_node.next_node = current_node.next_node
        current_node.next_node = insert_node
