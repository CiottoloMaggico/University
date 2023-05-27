def zero_two_partition(a):
    pivot = 2
    i = -1
    for j in range(len(a)):
        if a[j] <= pivot:
            i += 1
            if j > i:
                a[i], a[j] = a[j], a[i]

    return a

def partiziona(a, start, end):
    pivot = end
    i = start-1
    for j in range(start, end+1):
        if a[j] <= a[pivot]:
            i += 1
            if j > i:
                a[i], a[j] = a[j], a[i]
    return i

def quicksort(a, start, end):
    if start < end:
        mid = partiziona(a, start, end)
        quicksort(a, start, mid-1)
        quicksort(a, mid+1, end)

    return a

def srotola_ordina(a, m, n):
    tmp = []
    for i in range(m):
        for j in range(n):
            tmp += [a[i][j]]
    quicksort(tmp, 0, len(tmp)-1)
    return tmp

def ordina_matrici(a, m, n):
    tmp = srotola_ordina(a, m, n)
    k = 0
    for i in range(m):
        for j in range(n):
            a[i][j] = tmp[k]
            k += 1
    return a



print(f"Quicksort: {quicksort([1,23,34,676,3,5,89,12,43,766,76, 423, 45], 0, 12)}")
print(f"Srotola e ordina: {ordina_matrici([[1, 34, 2],[54, 32, 6],[654,12 ,34]], 3, 3)}")
print(f"zero/two: {zero_two_partition([0, 2, 0, 0, 0, 0, 2, 0, 2, 2, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 2, 0, 0, 2, 0, 0, 2, 2, 2, 0])}")