# zadanie 2 (KOLOS) - Merge-Sort (Zmodyfikowany)

import random


def mergeSort(tab):
    if len(tab) <= 1:
        return tab

    mid = len(tab) // 2  # dzielenie podloga
    lewa = mergeSort(tab[:mid])
    prawa = mergeSort(tab[mid:])
    i = j = 0
    wynik = []
    while i < len(lewa) and j < len(prawa):
        if (lewa[i][0] < prawa[j][0]) or (lewa[i][0] == prawa[j][0] and lewa[i][1] < prawa[j][1]):
            wynik.append(lewa[i])
            i += 1
        else:
            wynik.append(prawa[j])
            j += 1
    wynik.extend(lewa[i:])
    wynik.extend(prawa[j:])
    return wynik


doTestu = [[random.randint(1, 6), random.randint(1, 6)] for i in range(25)]
# doTestu2 = [[random.randint(1, 100), random.randint(1, 100)] for y in range(250)]


print("Posortowane elementy: ", mergeSort(doTestu))
