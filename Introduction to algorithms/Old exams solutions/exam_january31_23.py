# Ex 1

# Find the recurrence equation of "IndiciValori" algorithm

# Recurrence equation
#---------------------
# T(n) = 2T(n//2) + Theta(n^2)
# T(1) = Theta(1)
# --------------------

# Solved by both iterative and principal methods the solution is: Theta(n^2)

# Ex 2

# Write an algorithm "ElementoPiuFrequente" which find the most frequent element in an array of n elements with a value between [1, 10n]
# If most elements occurs the same times return the minimum element

def ElementoPiuFrequente(a):
    biggest = max(a)
    occurs = [0] * (biggest+1)
    for i in range(len(a)):
        occurs[a[i]] += 1
    max_occur = max(occurs)
    for i in range(len(occurs)):
        if occurs[i] == max_occur:
            return i
    return

# The Time complexity of this algorithm in the worst case is O(n) because the value of maximum element
# which can be in the array is linear with n
# So T(n) = Theta(n) + Theta(10n) = Theta(n)

# Test:
print(f"Valid: {ElementoPiuFrequente([2, 2, 1000, 10, 231, 213, 1230, 23, 34, 23, 23]) == 2}")
print(f"Valid: {ElementoPiuFrequente([2, 2, 2, 1000, 10, 231, 213, 1230, 23, 34, 23, 23]) == 2}")

# Ex 3

# Given a linkedlist write an algorithm which find the element that have a value equal to the sum of the element before.

def es3(node, sum=0):
    if node == None:
        return None
    if node.key == sum:
        return node.key
    return es3(node.next, sum+node.key)

# The time complexity of this recursive algorithm is find solving this recurrence equation:
#---------------------
# T(n) = T(n-1) + Theta(1)
# T(1) = Theta(1)
# --------------------

# Solving it with iterative method we found a time complexity of O(n) in the worst case
# and Omega(1) in the best case





















