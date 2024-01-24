from random import randint


def merge(array, p, m1, m2, k):
    p1 = m1
    pb = 0
    p0 = p
    b = [0 for i in range(k - p)]
    c0 = m1 - p
    c1 = m2 - m1
    while c0 > 0 and c1 > 0:
        if array[p0] <= array[p1]:
            b[pb] = array[p0]
            p0 += 1
            c0 -= 1
        else:
            b[pb] = array[p1]
            p1 += 1
            c1 -= 1
    while c0 > 0:
        b[pb] = array[p0]
        pb += 1
        p0 += 1
        c0 -= 1
    while c1 > 0:
        b[pb] = array[p1]
        pb += 1
        p1 += 1
        c1 -= 1
    pa = 0
    p0 = p
    c2 = k - m2
    q2 = m2
    while pb > 0 and c2 > 0:
        if b[pa] <= array[q2]:
            array[p0] = array[pa]
            p0 += 1
            pa += 1
            pb -= 1
        else:
            array[p0] = array[q2]
            p0 += 1
            q2 += 1
            c2 -= 1
    while pb > 0:
        array[p0] = b[pa]
        p0 += 1
        pa += 1
        pb -= 1


def mergesort(array, p, k):
    if p < k - 1:
        m1 = (2 * p + k) // 3
        m2 = (p + 2 * k) // 3
        mergesort(array, p, m1)
        mergesort(array, m1, m2)
        mergesort(array, m2, k)
        merge(array, p, m1, m2, k)


tablica = [[randint(1,6), randint(1,6)] for i in range(25)]
print("Tablica przed posortowaniem: ", tablica)
mergesort(tablica, 0 , len(tablica) - 1)
print("Tablica po pierwszym sortowaniu: ", tablica)
