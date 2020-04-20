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

def fastFib(n, memo = {}):
    """Assumes n is an int >= 0, memo used only by recursive calls 
        Returns Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    try: 
        return memo[n]
    except KeyError:
        result = fastFib(n-1, memo) + fastFib(n-1, memo)
        memo[n] = result
        return result

# This version of the Fibonacci algorithm uses the dynamic programming technique of memoization to save
# computations that have already been performed, which makes subsequent calculations faster to complete.

