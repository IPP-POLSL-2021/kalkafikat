import random

def merge_sort_3_way(arr, p, k):
    if p < k - 1:
        m1 = (2 * p + k) // 3
        m2 = (p + 2 * k) // 3
        merge_sort_3_way(arr, p, m1)
        merge_sort_3_way(arr, m1, m2)
        merge_sort_3_way(arr, m2, k)
        merge(arr, p, m1, m2, k)

def merge(arr, p, m1, m2, k):
    p1 = m1
    pb = 0
    p0 = p
    b = [0] * (k - p)
    c0 = m1 - p
    c1 = m2 - m1
    while c0 > 0 and c1 > 0:
        if arr[p0] <= arr[p1]:
            b[pb] = arr[p0]
            p0 += 1
            c0 -= 1
        else:
            b[pb] = arr[p1]
            p1 += 1
            c1 -= 1
        pb += 1
    while c0 > 0:
        b[pb] = arr[p0]
        p0 += 1
        c0 -= 1
        pb += 1
    while c1 > 0:
        b[pb] = arr[p1]
        p1 += 1
        c1 -= 1
        pb += 1
    pa = 0
    p0 = p
    c2 = k - m2
    q2 = m2
    while pb > 0 and c2 > 0:
        if b[pa] <= arr[q2]:
            arr[p0] = b[pa]
            pa += 1
            pb -= 1
        else:
            arr[p0] = arr[q2]
            q2 += 1
            c2 -= 1
        p0 += 1
    while pb > 0:
        arr[p0] = b[pa]
        pa += 1
        pb -= 1

arr = [[random.randint(1,6), random.randint(1,6)] for _ in range(25)]
print(f"Przed sortowaniem: {arr}")
merge_sort_3_way(arr, 0, len(arr))
merge_sort_3_way(arr, 0, len(arr))
merge_sort_3_way(arr, 0, len(arr))
print(f"Posortowane: {arr}")
