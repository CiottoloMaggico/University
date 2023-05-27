from data_structures import Stack, Queue, Node
import random

class NonSenseQueue():
    """Exercise 1: emulate a queue using two stacks"""
    def __init__(self, node=None):
        self.first_stack = Stack(node)
        self.second_stack = Stack()

    def __repr__(self):
        return f"First Stack: {self.first_stack} \nSecond Stack: {self.second_stack}"

    def push(self, k):
        self.first_stack.push(k)

    def pop(self):
        curr = self.first_stack.pop()
        if type(curr) == str:
            return "ERROR: the queue is empty"
        while curr.next != None:
            curr.next = None
            self.second_stack.push(curr)
            curr = self.first_stack.pop()
        popped = curr
        curr = self.second_stack.pop()
        if type(curr) == str:
            return "ERROR: the queue is empty"
        while curr.next != None:
            curr.next = None
            self.first_stack.push(curr)
            curr = self.second_stack.pop()
        self.first_stack.push(curr)

        return popped
def create_stack(n):
    head = Node(random.randint(0, 1000))
    stack = Stack(head)
    for i in range(1, n):
        stack.push(Node(random.randint(0, 1000)))
    return stack

def create_queue(n):
    head = Node(random.randint(0, 1000))
    queue = Queue(head)
    for i in range(1, n):
        queue.push(Node(random.randint(0, 1000)))
    return queue

def create_nonsense_queue(n):
    head = Node(random.randint(0, 1000))
    nonsense_queue = NonSenseQueue(head)
    for i in range(1, n):
        nonsense_queue.push(Node(random.randint(0, 1000)))
    return nonsense_queue


if __name__ == "__main__":
    my_stack = create_stack(10)
    my_queue = create_queue(10)
    print(f"Stack: {my_stack}\n")
    print(f"Queue: {my_queue}\n")

    # Test queue push
    user_input = input("Do you want to join a random element to the queue? [y/n]")
    while user_input != "n":
        user_input = input("Insert?: [n to exit] ")
        if user_input == "n":
            break
        to_insert = Node(random.randint(0, 1000))
        print(f"I will insert: {to_insert}")
        my_queue.push(to_insert)
        print(f"Inserted!\n\t{my_queue}")

    # Test queue pop
    user_input = input("Do you want to pop element from the queue? [y/n] ")
    while user_input != "n":
        print(my_queue)
        user_input = input("Pop?: [n per uscire] ")
        if user_input == "n":
            break
        my_queue.pop()
        print(f"{my_queue}\n")

    # Test stack push
    user_input = input("Do you want to join a random element to the stack? [y/n]")
    while user_input != "n":
        user_input = input("Insert?: [n to exit] ")
        if user_input == "n":
            break
        to_insert = Node(random.randint(0, 1000))
        print(f"I will insert: {to_insert}")
        my_stack.push(to_insert)
        print(f"Inserted!\n\t{my_stack}")

    # Test stack pop
    user_input = input("Do you want to pop element from the stack? [y/n] ")
    while user_input != "n":
        print(my_stack)
        user_input = input("Pop?: [n per uscire] ")
        if user_input == "n":
            break
        my_stack.pop()
        print(f"{my_stack}\n")

    # Test nonsense-queue
    my_nonsense_queue = create_nonsense_queue(10)
    # Test nonsense-queue push
    user_input = input("Do you want to join a random element to the nonsense-queue? [y/n]")
    while user_input != "n":
        user_input = input("Insert?: [n to exit] ")
        if user_input == "n":
            break
        to_insert = Node(random.randint(0, 1000))
        print(f"I will insert: {to_insert}")
        my_nonsense_queue.push(to_insert)
        print(f"Inserted!\n\t{my_nonsense_queue}")

    # Test nonsense-queue pop
    user_input = input("Do you want to pop element from the nonsense-queue? [y/n] ")
    while user_input != "n":
        print(f"Before: {my_nonsense_queue}")
        user_input = input("Pop?: [n per uscire] ")
        if user_input == "n":
            break
        popped = my_nonsense_queue.pop()
        print(f"Removed: {popped}\n")

