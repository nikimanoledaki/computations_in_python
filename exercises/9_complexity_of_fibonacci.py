def fib_iter(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_i = 0 
        fib_ii = 1 # Setting up 2 previous numbers
        for i in range(n-1):
            tmp = fib_i 
            fib_i = fib_ii
            fib_ii = tmp + fib_ii
        return fib_ii

# Best case: O(1)
# Worst case: O(1) + O(n) + O(1) => O(n)


def fib_recur(n):
    """" Assumes n an int >= 9 """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recur(n-1) + fib_recur(n-2)

# Exponential growth O(c^n) where c is the golden ratio to the nth power
