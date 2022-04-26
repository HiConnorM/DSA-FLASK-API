# Node class to create the nodes which store the data and pointer
class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


# Wrapper for Linked List class to create the linked list head and tail.
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

# for creating the array(list for python) that will store the user data in a list from a dictionary
    def to_list(self):
        l = []
        if self.head is None:
            return l

        node = self.head
        while node:
            l.append(node.data)
            node = node.next_node
        return l

# for printing Linked List

    def print_ll(self):
        ll_string = ""
        node = self.head
        if node is None:
            print("Linked List Empty")
        while node:
            ll_string += f" {str(node.data)} ->"
            node = node.next_node

        ll_string += " None"
        print(ll_string)

# Linked List Insert at beginning:

    def insert_beginning(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head

        new_node = Node(data, self.head)
        self.head = new_node

# Linked List Insert at end:
    def insert_at_end(self, data):
        if self.head is None:
            self.insert_beginning(data)
            return

        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node.next_node

# To get one user id
    def get_user_by_id(self, user_id):
        node = self.head
        while node:
            if node.data["id"] is int(user_id):
                return node.data
            node = node.next_node
        return None



