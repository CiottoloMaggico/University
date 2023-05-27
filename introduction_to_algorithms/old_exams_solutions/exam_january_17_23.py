# Ex 1

# Find a value a for the following recurrence equation that the time complexity of the equation not exceed
# Theta(n^3)

# Recurrence equation
#---------------------
# T(n) = aT(n//2) + Theta(sqrt(n))
# T(1) = Theta(1)
# ! a >= 2
# --------------------

# Solve the inequality n^(log2(a)) < n^3 give us the answer, so for not exceed Theta(n^3) the value of constant
# a must be less than 8

# Ex 2

# Write an algorithm "SottoSeq" which tell us if a subarray B is in the main array A.
# The algorithm return 1 if the subarray B occurs in the main array else it returns 0.

def SottoSeq(a, b):
    i = 0
    n, m = len(a), len(b)
    while i < n and a[i] != b[0]:
        i += 1
    if i == n: return 0
    j = 0
    while i < n and j < m and a[i] == b[j]:
        i += 1
        j += 1
    if j == m: return 1
    return 0

# So T(n) = Theta(n) + Theta(m) => [ m < n ] => T(n) = Theta(n)

# Test:
print(f"Valid: {SottoSeq([10, 20, 30, 40, 1, 56, 75, 123, 3], [10, 20, 30, 40])}")
print(f"Valid: {SottoSeq([45, 563, 123, 4,23, 324], [1])}")

# Ex 3

# Write an algorithm that check if all elements in a binary tree are the same

def es3(node, val=None):
    if node == None:
        return 1
    if val == None:
        return es3(node.right, node.key) * es3(node.left, node.key)
    if node.key != val:
        return 0
    return es3(node.right, val) * es3(node.left, val)

# The time complexity of this recursive algorithm is find solving this recurrence equation:
#---------------------
# T(n) = T(k) + T(n-1-k) + Theta(1)
# T(1) = Theta(1)
# --------------------

















