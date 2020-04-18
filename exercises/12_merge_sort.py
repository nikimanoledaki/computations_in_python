def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result

def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else: 
        middle = len(L)//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

# Complexity of Merge Sort
# At first recursion level: n/2 elements in each list => O(n) + O(n) = O(n) where n is len(L)
# At second recursion level: n/4 elements in each list => two merges => O(n) where n is len(L)
# Each recursion level if O(n) where n is len(L)
# Dividing list in half with each recursive call => O(log (n)) where n is Len(L)
# Therefore, overall algorithmic complexity of merge sort is O(n log n). This is the best worst-case for a sorting algorithm.