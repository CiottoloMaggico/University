import data_structures
import random

def create_linkedlist(n):
    head = linkedlist.Node(random.randint(0, 1000))
    list = linkedlist.LinkedList(head)
    current = head
    for i in range(1, n):
        current.next = linkedlist.Node(random.randint(0, 1000))
        current = current.next
    return list

def insertion_sort(a):
    n = len(a)
    for i in range(1, n, +1):
        x = a[i]
        j = i - 1
        while ((j >= 0) and (a[j].key > x.key)):
            a[j+1] = a[j]
            j -= 1
        a[j+1] = x
    return a


# ex 1
# A
def to_last(p):
    tmp = p.head
    while tmp.next != None:
        tmp = tmp.next
    return tmp

# B
def to_secondlast(p):
    tmp = p.head
    while tmp.next.next != None:
        tmp = tmp.next
    return tmp

# C
def delete_last(p):
    tmp = to_secondlast(p)
    tmp.next = None

# ex 2
# A
def reverse_linkedlist(p):
    nxt, curr, prev = None, p.head, p.head.next
    while prev != None:
        curr.next = nxt
        nxt = curr
        curr = prev
        prev = curr.next
    curr.next = nxt
    p.head = curr

# B
def odd_even_list(p):
    lk_odd, lk_even = linkedlist.LinkedList(p.head.next), linkedlist.LinkedList(p.head)
    odd, even = p.head.next, p.head
    while ((odd != None) and (even != None)):
        even.next = odd.next
        even = even.next
        if even == None:
            break
        odd.next = even.next
        odd = odd.next
    return lk_odd, lk_even

# ex 3
# A
def insert_sorted(p, k):
    curr = p.head
    nxt = curr.next
    if k.key < curr.key:
        k.next = curr
        p.head = k
        return
    while nxt != None:
        if curr.key <= k.key < nxt.key:
            curr.next = k
            k.next = nxt
            return
        curr = nxt
        nxt = nxt.next
    curr.next = k

# B
def sort_linkedlist(p):
    to_arr = []
    curr = p.head
    while curr != None:
        to_arr += [curr]
        curr = curr.next
    to_arr = insertion_sort(to_arr)
    p.head = to_arr[0]
    to_arr[-1].next = None
    for i in range(1, len(to_arr)):
        to_arr[i-1].next = to_arr[i]


if __name__ == "__main__":
    my_linkedlist = create_linkedlist(10)

    # Test insertion
    new_node = linkedlist.Node(random.randint(0, 1000))
    print(f"Before: {my_linkedlist}\n")
    my_linkedlist.insert(new_node)
    print(f"After: {my_linkedlist}\n")

    print("\n"*3)

    # Test deletion
    user_input = input("Vuoi cancellare elementi dalla linkedlist? [s/n] ")
    while user_input != "n":
        print(my_linkedlist)
        user_input = input("Inserisci il numero da rimuovere: [n per uscire] ")
        if user_input == "n":
            break
        my_linkedlist.delete(int(user_input))

    print("\n" * 3)

    # Test ex 1
    print("ES 1 A: Controlla se l'ultimo numero corrisponde:")
    print(f"\t{my_linkedlist}")
    print(f"\t{to_last(my_linkedlist).key}\n")

    print("ES 1 B: Controlla se il penultimo numero corrisponde:")
    print(f"\t{my_linkedlist}")
    print(f"\t{to_secondlast(my_linkedlist).key}\n")

    print("ES 1 C: Controlla se l'ultimo elemento è stato cancellato:")
    print(f"\t{my_linkedlist}")
    delete_last(my_linkedlist)
    print(f"\t{my_linkedlist}\n")

    # Test ex 2
    print("ES 2 A: Controlla se la linkedlist è stata invertita correttamente:")
    print(f"\t{my_linkedlist}")
    reverse_linkedlist(my_linkedlist)
    print(f"\t{my_linkedlist}\n")

    print("ES 2 B: Controlla se le linked list sono state create correttamente:")
    print(f"\t{my_linkedlist}")
    odd, even = odd_even_list(my_linkedlist)
    print(f"\tDispari: {odd}\n\tPari: {even}\n")

    # Test ex 3
    print("ES 3 A: Controlla se la linkedlist è ordinata correttamente:")
    print(f"\t{my_linkedlist}")
    sort_linkedlist(my_linkedlist)
    print(f"\t{my_linkedlist}\n")

    print("ES 3 B: Controlla se l'elemento è stato inserito correttamente:")
    while True:
        print(f"\t{my_linkedlist}")
        to_insert = input("Scrivi il numero da inserire: [n per uscire] ")
        if to_insert == "n":
            break
        insert_sorted(my_linkedlist, linkedlist.Node(int(to_insert)))
        print(f"\n\t{my_linkedlist}\n")
