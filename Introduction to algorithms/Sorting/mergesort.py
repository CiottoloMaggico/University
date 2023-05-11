def merge(a, start, mid, end):
    i, j = start, mid+1
    tmp = []
    while ((i <= mid) and (j <= end)):
        if a[i] <= a[j]:
            tmp += [a[i]]
            i += 1
        else:
            tmp += [a[j]]
            j += 1
    if i <= mid:
        tmp += a[i:mid+1]
    elif j <= end:
        tmp += a[j:end+1]

    for k in range(len(tmp)):
        a[start+k] = tmp[k]

def recursive_merge(a, start, mid, end, tmp, i, j):
    if not ((i <= mid) and (j <= end)):
        if i <= mid:
            tmp += a[i:mid+1]
        elif j <= end:
            tmp += a[j:end+1]
        for k in range(len(tmp)):
            a[start+k] = tmp[k]
        return
    if a[i] <= a[j]:
        tmp += [a[i]]
        recursive_merge(a, start, mid, end, tmp, i+1, j)
    else:
        tmp += [a[j]]
        recursive_merge(a, start, mid, end, tmp, i, j+1)

def four_merge(a, start, rmid, mid, lmid, end):
    merge(a, start, rmid, mid)
    merge(a, mid+1, lmid, end)
    merge(a, start, mid, end)


def recursive_mergesort(a, start, end):
    if start < end:
        mid = (start + end)//2
        recursive_mergesort(a, start, mid)
        recursive_mergesort(a, mid+1, end)
        recursive_merge(a, start, mid, end, [], start, mid+1)
    return a

def iterative_mergesort(a):
    width = 1
    n = len(a)
    while (width < n):
        start = 0
        while (start < n):
            end = min(start+(2*width-1), n-1)
            mid = min((start+end)//2, n-1)

            merge(a, start, mid, end)
            start += 2*width
        width *= 2

    merge(a, 0, width//2-1, n-1)
    return a

def four_mergesort(a, start, end):
    if start >= end:
        return a
    mid = (start + end)//2
    rmid = (start+mid)//2
    lmid = (mid+end+1)//2
    four_mergesort(a, start, rmid)
    four_mergesort(a, rmid+1, mid)
    four_mergesort(a, mid+1, lmid)
    four_mergesort(a, lmid+1, end)
    four_merge(a, start, rmid, mid, lmid, end)
    return a

print(f"Recursive MergeSort: {recursive_mergesort([12, 1, 23, 45, 655, 43, 65, 11, 2, 3, 4], 0, 10)}")
print(f"Iterative MergeSort: {iterative_mergesort([12, 1, 23, 45, 655, 43, 65, 11, 4, 3, 2])}")
print(f"Four Mergesort: {four_mergesort([12, 1, 23, 45, 655, 43, 65, 11, 2, 3, 4], 0, 10)}")