class Node():
    def __init__(self, key=None, next=None):
        self.key = key
        self.next = next

    def __repr__(self):
        return str(self.key)

class LinkedList():
    def __init__(self, node=None):
        self.head = node

    def __repr__(self):
        if self.head is None:
            return "The list is empty!"
        curr = self.head
        string = ""
        while curr != None:
            string += f"{curr.key} --> "
            curr = curr.next
        string += "None"
        return string

    def insert(self, k):
        if self.head is None:
            self.head = k
            return k
        k.next = self.head
        self.head = k
        return k

    def __len__(self):
        if self.head is None:
            return 0
        curr = self.head
        counter = 1
        while curr.next != None:
            counter += 1
            curr = curr.next
        return counter

    def delete(self, k_key):
        if self.head is None:
            return "ERROR: the list is empty!"
        prev = None
        curr = self.head
        while curr != None:
            if curr.key == k_key:
                if prev == None:
                    self.head = curr.next
                else:
                    prev.next = curr.next
                return
            prev = curr
            curr = curr.next

class Stack(LinkedList):
    """Stack witch use a linkedlist as base data structure"""
    def __init__(self, node=None):
        self.head = node

    def push(self, k):
        if self.head is None:
            self.head = k
            return
        k.next = self.head
        self.head = k

    def pop(self):
        if self.head is None:
            return "ERROR: the stack is empty!"
        old_top = self.head
        self.head = self.head.next
        return old_top

class Queue(LinkedList):
    """Queue witch use a linkedlist as base data structure"""
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def push(self, k):
        if self.tail is None or self.head is None:
            self.tail = k
            self.head = k
            return
        old_tail = self.tail
        self.tail = k
        old_tail.next = self.tail

    def pop(self):
        if self.tail is None or self.head is None:
            return "ERROR: the queue is empty!"
        old_head = self.head
        self.head = old_head.next
        return old_head

class ArrayStack():
    """Stack witch use an array as base data structure"""
    def __init__(self, size):
        self.data = [None]*(size-1)
        self.top = -1

    def __repr__(self):
        return str(self.data)

    def push(self, k):
        self.top += 1
        self.data[self.top] = k

    def pop(self):
        deleted = self.data[self.top]
        self.data[self.top] = None
        self.top -= 1
        return deleted

class ArrayQueue():
    """Queue witch use an array as base data structure"""
    def __init__(self, size):
        self.size = size
        self.data = [None]*(size)
        self.head = -1
        self.tail = 0

    def __repr__(self):
        return str(self.data)

    def enqueue(self, k):
        if self.head == self.size-1 and self.tail == 0:
            return "ERROR: the queue is full!"
        if self.head + 1 == self.tail and self.tail != 0:
            return "ERROR: the queue is full!"
        if self.head == self.size-1:
            self.head = 0
        else:
            self.head += 1
        self.data[self.head] = k

    def dequeue(self):
        if self.head == -1:
            return "ERROR: The queue is empty!"
        if self.head == self.tail and self.data[self.tail] != None:
            return "ERROR: The queue is empty!"
        deleted = self.data[self.tail]
        self.data[self.tail] = None
        if self.tail == self.size-1:
            self.tail = 0
        else:
            self.tail += 1
        return deleted
