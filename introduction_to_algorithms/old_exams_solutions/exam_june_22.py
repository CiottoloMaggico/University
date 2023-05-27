# Ex 2

def ex_2(a, s):
    i, j = 0, 0
    queue_sum = a[i]
    n = len(a)
    while i < n and j < n-1:
        if queue_sum == s:
            return (i,j)
        elif queue_sum < s:
            j += 1
            queue_sum += a[j]
        else:
            queue_sum -= a[i]
            if i == j:
                i += 1
                j += 1
            else:
                i += 1
    while i < n:
        if queue_sum == s:
            return (i,j)
        queue_sum -= a[i]
        i += 1
    return None

# Test:
print(ex_2([1,3,5,2,9,3,3,1,6], 21))
print(ex_2([1,3,5,2,9,3,3,1,6], 7))
print(ex_2([1,3,5,2,9,3,3,1,6], 8))
print(ex_2([1,3,5,2,9,3,3,1,6], 12))
print(ex_2([1,3,5,2,9,3,3,1,6], 1))

# Ex 3

def ex_3(linkedlist):
    prev = linkedlist.head.next
    curr = linkedlist.head
    next = None
    while prev != None:
        if curr.key > 10:
            tmp_prev = prev.next
            prev.next = next
            curr = prev
            prev = tmp_prev
        else:
            tmp_prev = prev.next
            prev.next = curr
            next = curr
            curr = prev
            prev = tmp_prev
    linkedlist.head = curr





