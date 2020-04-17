def isSubset(L1, L2):
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                print('Matched', e1)
                break
        if not matched:
            return False
    return True


L1 = (1, 2)
L2 = (1, 2)
isSubset(L1, L2)

# Outer loop executed len(L1) times
# Each iteration will execute inner loop up to len(L2) times, with constant number of operations
# O(fn(L1)) * O(fn(L2)) = O(fn(L1) * fn(L2)) - Law of Multiplication for O()
# Therefore: O(n^2)
