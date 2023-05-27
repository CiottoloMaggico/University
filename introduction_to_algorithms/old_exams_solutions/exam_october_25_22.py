# Ex 1
import random


# Find and solve the recurrence relation of given algorithm and if its possible solve it with principal method
# Answer:
#---------------------
# T(n) = 2T(n/2) + Theta(n/log(n))
# T(1) = Theta(1)
# --------------------
#The related recurrence equation can't be solved by principal method

# Ex 2
# Write an algorithm "even_odd" which order the given array moving all even in the even position and all the odds in odd position.

def even_odd_checker(a):
    for i in range(len(a)):
        if a[i]%2 != i%2:
            return False
    return True

def even_odd(a):
    n = len(a)
    even, odd = 0, 1

    while even < n and odd < n:
        if a[even] % 2 == 0:
            even += 2
        elif a[odd] % 2 == 1:
            odd += 2
        else:
            a[even], a[odd] = a[odd], a[even]
            odd += 2
            even += 2
    return a

# So T(n) = Theta(n)

# Test:
array_len = 13
array = [1]*(array_len//2) + [2]*(array_len//2)
array_2 = [7,3,1,8,8,2,1,4]
result = even_odd(array_2)
print(f"{list(range(array_len))}\n{result}\nIs valid? {even_odd_checker(result)}")

# Ex 3

# Write an algorithm that find the minimum in a circular linkedlist

def es3(node):
    curr = node.next
    min = node.key
    while curr.key != node.key:
        if curr.key < min:
            min = curr.key
        curr = curr.next
    return min

# The time complexity of this recursive algorithm is Theta(n)

















