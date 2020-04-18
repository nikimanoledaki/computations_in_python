def bisect_search(L, e):
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L)//2
        if L[half] > e:
            return bisect_search(L[:half], e)
        else:
            return bisect_search(L[half:], e)


L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
e = 2
bisect_search(L, 2)
