def heapify(a, i, heap_size):
    left, right, new_root = 2*i+1, 2*i+2, i
    if left < heap_size:
        if a[left] > a[i]:
            new_root = left
    if right < heap_size:
        if a[right] > a[new_root]:
            new_root = right
    if new_root != i:
        a[i], a[new_root] = a[new_root], a[i]
        heapify(a, new_root, heap_size)

def reversed_heapify(a, i):
    father = (i-1)//2
    if father <= 0:
        return
    if a[i] > a[father]:
        a[i], a[father] = a[father], a[i]
        reversed_heapify(a, father)
    

def build_heap(a):
    heap_size = len(a)
    for i in range((heap_size//2), -1, -1):
        heapify(a, i, heap_size)

    return a

def heap_sort(a):
    build_heap(a)
    for i in range(len(a)-1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapify(a, 0, i)

    return a

def reverse_heap_sort(a):
    build_heap(a)
    for i in range(len(a) - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapify(a, 0, i)
    for i in range(len(a)//2):
        a[i], a[-(i+1)] = a[-(i+1)], a[i]

    return a

def lowest(a):
    build_heap(a)
    n = len(a)
    lowst = a[n-1]
    for i in range(1, ((n+1)//2)):
        if a[n-i] < lowst:
            lowst = a[n-i]
    return lowst

def insert_heap(a, i):
    build_heap(a)
    a += [i]
    reversed_heapify(a, len(a)-1)
    return a

print(f"Heap sort: {heap_sort([5, 123, 231,53,45, 213, 453, 3214, 1, 34, 321, 457, 787,3,323, 33,4546,8 ,342, 20])}")
print(f"Reversed: {reverse_heap_sort([5, 123, 231,53,45, 213, 453, 3214, 1, 34, 321, 457, 787,3,323, 33,4546,8 ,342, 20])}")
print(f"--"*50)
print(f"Lowest: {lowest([5, 123, 231,53,45, 213, 453, 3214, 1, 34, 321, 457, 787,3,323, 33,4546,8 ,342])}")
print(f"--"*50)
print(f"Insert: {insert_heap([5, 123, 231,53,45, 213, 453, 3214, 1, 34, 321, 457, 787,3,323, 33,4546,8], 342)}")
print(f"Expected: {build_heap([5, 123, 231,53,45, 213, 453, 3214, 1, 34, 321, 457, 787,3,323, 33,4546,8 ,342])}")
