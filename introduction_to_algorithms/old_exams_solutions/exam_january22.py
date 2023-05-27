# Ex 1

# Find the time complexity of the following recursive algorithm
#
# Recurrence equation
# -------------------
# T(n) = T(n-2) + Theta(1)
# T(1) = Theta(1)
# -------------------
# If we solve it with Three Method we find T(n) = summation from 1 to n/2 of Theta(1) == Theta(n)

# Ex 2

# We have two increasing order arrays of n distinct integers,
# check if there is at least one value in A and one value in B
# that |x-y| <= 3. Return 1 if True else 0
# Solve the problem with a Time Complexity lower than Theta(n^2)

def modb_search(a, x, l, h):
    if l >= h:
        return l
    m = (l+h)//2
    if a[m] == x:
        return m
    if a[m] > x:
        return modb_search(a, x, l, m-1)
    return modb_search(a, x, m+1, h)

def ex_2(a, b):
    for i in range(len(a)):
        x = a[i]
        y = b[modb_search(b, x, 0, len(b)-1)]
        if abs(x-y) <= 3:
            return 1
    return 0

# The Time Complexity is Theta(nlog(n)) so lesser than Theta(n^2)

# Test
array_a = [1,2,9,10,12]
array_b = [6,14,16,20]
print(ex_2(array_a, array_b))

# Ex 3
from introduction_to_algorithms.data_structures.data_structures import LinkedList
from introduction_to_algorithms.data_structures.eslinkedlist import create_linkedlist, sort_linkedlist

# Write an algorithm with Theta(n) of Time Complexity that remove all the duplicates from
# an increasing order linkedlist

def ex_3(node):
    prev = node
    curr = node.next
    while curr != None:
        if curr.key != prev.key:
            prev.next = curr
            prev = prev.next
        curr = curr.next
    prev.next = None
    return node

def ex_3_ric(node, prev=None):
    if prev == None:
        prev = node
        node = node.next
    if node == None:
        prev.next = None
        return
    if node.key != prev.key:
        prev.next = node
        ex_3_ric(node.next, node)
    else:
        ex_3_ric(node.next, prev)

# Test
my_list = create_linkedlist(20)
sort_linkedlist(my_list)
print(my_list)
ex_3_ric(my_list.head)
print(my_list)