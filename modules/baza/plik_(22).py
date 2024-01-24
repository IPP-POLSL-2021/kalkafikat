import random


def szybkieSortowaniePivotSmieszny(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-3] if len(arr) >= 3 else arr[-1]
    smaller, equal, larger = [], [], []
    for val in arr:
        if val[0] < pivot[0]:
            smaller.append(val)
        elif val[0] == pivot[0]:
            equal.append(val)
        else:
            larger.append(val)
    return szybkieSortowaniePivotSmieszny(smaller) + equal + szybkieSortowaniePivotSmieszny(larger)


arr = [(random.randint(0, 10), random.randint(0, 10)) for i in range(50)]
sorted_arr = szybkieSortowaniePivotSmieszny(arr)

print("Przed sortowaniem: ")
print(arr)
print(" ")
print("Po sortowaniu: ")
print(sorted_arr)
