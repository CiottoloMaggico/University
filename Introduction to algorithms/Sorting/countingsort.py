def countingsort(a):
    k = max(a)
    occurrences = [0]*(k+1)
    for i in a:
        occurrences[i] += 1
    j = 0
    for i in range(len(occurrences)):
        while occurrences[i] > 0:
            a[j] = i
            occurrences[i] -= 1
            j += 1
    return a

def carry_countingsort(a):
    k = max(a)
    occurrences = [0]*(k+1)
    final = [0]*(len(a))
    print(len(a), len(final))
    for i in a:
        occurrences[i] += 1
    for i in range(1, len(occurrences)):
        occurrences[i] += occurrences[i-1]
    for i in a:
        final[occurrences[i]-1] = i
        occurrences[i] -= 1

    return final

def insertion_sort(a):
    n = len(a)
    for i in range(1, n, +1):
        x = a[i]
        j = i - 1
        while ((j >= 0) and (a[j] > x)):
            a[j+1] = a[j]
            j -= 1
        a[j+1] = x
    return a

def bucket_sort(a, n):
    k = max(a)
    h = k//n
    buckets = [[] for _ in range(n+1)]
    for i in range(len(a)):
        buckets[(a[i]//h)] += [a[i]]
    final = []
    for i in range(n+1):
        final += insertion_sort(buckets[i])

    return final



# print(f"Bucket sort: {bucket_sort([1, 4, 5, 12, 2, 8, 6, 3, 6, 9, 10, 11, 16, 19, 32, 20, 21, 23, 24], 2)}")

# carry_counting_sort = carry_countingsort([12,2143,42,21,21,5,4,1,21,213,45,56,34,2,7,98,665,6,5,2321])
# counting_sort = countingsort([12,2143,42,21,21,5,4,1,21,213,45,56,34,2,7,98,665,6,5,2321])
# print(f"Counting sort: {counting_sort}")
# print(f"Carry counting sort: {carry_counting_sort}")
# print(f"Equals ? {counting_sort == carry_counting_sort}")