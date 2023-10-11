class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class link_list:

    def __init__(self):
        self.head = None  # head is a label to show the start of the linked list

    def Insert_first(self, new_data):
        new_node = Node(new_data)  # create an object from the class of Node
        new_node.next = self.head  # head should connect to the new node
        self.head = new_node  # head should be in the first of the liked list, #so, new_node takes the label of the head

    def insert_last(self, new_data):
        new_node = Node(new_data)
        if self.head is None:  # if there is not any node on the linked list
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_between(self, prev_data, new_data):
        if prev_data is None:
            print("previous node does not exist!")

        new_node = Node(new_data)
        new_node.next = prev_data.next
        prev_data.next = new_node

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


first_node = Node(1)
second_node = Node(2)
third_node = Node(3)
forth_node = Node(4)
mylist = link_list()
mylist.head = first_node
mylist.head.next = second_node
second_node.next = third_node
third_node.next = forth_node
mylist.traverse()
mylist.insert_between(second_node, 7)
mylist.insert_last(12)
mylist.traverse()

