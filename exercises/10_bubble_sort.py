def bubble_sort(L):
    swap = False
    while not swap:
        print(str(L))
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp

# inner for loop is doing comparisons
# outer while loop is doing multiple passes until no more swaps
