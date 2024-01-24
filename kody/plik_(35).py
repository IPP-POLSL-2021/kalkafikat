# ZADANIE 2
import random


def merge(tab1, lewa, mid1, mid2, prawa, tab2):
    i = lewa
    j = mid1
    k = mid2
    w = lewa

    while (i < mid1) and (j < mid2) and (k < prawa):
        if tab1[i] < tab1[j]:
            if tab1[i] < tab1[k]:
                tab2[w] = tab1[i]
                w += 1
                i += 1
            else:
                tab2[w] = tab1[k]
                w += 1
                k += 1
        else:
            if tab1[j] < tab1[k]:
                tab2[w] = tab1[j]
                w += 1
                j += 1
            else:
                tab2[w] = tab1[k]
                w += 1
                k += 1

    while (i < mid1) and (j < mid2):
        if tab1[i] < tab1[j]:
            tab2[w] = tab1[i]
            w += 1
            i += 1
        else:
            tab2[w] = tab1[j]
            w += 1
            j += 1

    while (j < mid2) and (k < prawa):
        if tab1[j] < tab1[k]:
            tab2[w] = tab1[j]
            w += 1
            j += 1
        else:
            tab2[w] = tab1[k]
            w += 1
            k += 1

    while (i < mid1) and (k < prawa):
        if tab1[i] < tab1[k]:
            tab2[w] = tab1[i]
            w += 1
            i += 1
        else:
            tab2[w] = tab1[k]
            w += 1
            k += 1

    while i < mid1:
        tab2[w] = tab1[i]
        w += 1
        i += 1

    while j < mid2:
        tab2[w] = tab1[j]
        w += 1
        j += 1

    while k < prawa:
        tab2[w] = tab1[k]
        w += 1
        k += 1


def mergeSort3WayRec(tab1, lewa, prawa, tab2):
    if prawa - lewa < 2:
        return

    mid1 = lewa + ((prawa - lewa) // 3)
    mid2 = lewa + 2 * ((prawa - lewa) // 3) + 1

    mergeSort3WayRec(tab2, lewa, mid1, tab1)
    mergeSort3WayRec(tab2, mid1, mid2, tab1)
    mergeSort3WayRec(tab2, mid2, prawa, tab1)

    merge(tab2, lewa, mid1, mid2, prawa, tab1)


def mergeSort3Way(tab1):
    n = len(tab1)
    if n == 0:
        return

    tabpom = tab1.copy()

    mergeSort3WayRec(tabpom, 0, n, tab1)

    tab1 = tabpom.copy()

    return tab1


tab = [[random.randint(1, 6), random.randint(1, 6)] for i in range(25)]
print("Przed sortowaniem: ", tab)
tab = mergeSort3Way(tab)
print("Po sortowaniu:     ", tab)
