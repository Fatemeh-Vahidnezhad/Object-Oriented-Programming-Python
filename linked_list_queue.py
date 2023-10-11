class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.rear = None
        self.front = None

    def is_empty(self):
        return self.front is None

    def Enqueue(self, new_data):
        new_node = Node(new_data)
        if self.front is None:
            self.rear = self.front = new_node
            # print("first:",self.front.data)
            return
        self.rear.next = new_node
        self.rear = new_node

    def traverse(self):
        temp = self.front
        while temp:
            print(temp.data)
            temp = temp.next

    def Dequeue(self):
        if self.is_empty() is None:
            return "Queue does not have None!"
        temp = self.front  # assign self.front to a new variable
        self.front = temp.next
        if self.front is None:
            self.rear = None

'''
q = Queue()
q.Enqueue(4)
q.Enqueue(6)
q.Enqueue(8)
q.Enqueue(12)
q.traverse()
q.Dequeue()
print("*****")
q.traverse()
print(str(q.front.data), str(q.rear.data))
'''
# there is a module in the python that it is similar with the above class

from queue import Queue

q = Queue(maxsize=0)  # 0: unlimited members
q.put(1)
q.put(3)
q.put(0)
# q.put_nowait(100)
print(q.full())


########################
from collections import deque

q = deque()
q.append(5)
q.append(3)
print(q)
q.append(11)
q.popleft()
print(q)
