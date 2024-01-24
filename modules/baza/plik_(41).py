import random


def merge_sort(arr):
    if len(arr) > 1:
        m = len(arr) // 2
        l = arr[:m]
        r = arr[m:]
        merge_sort(l)
        merge_sort(r)
        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1


arr = [[random.randint(1, 6), random.randint(1, 6)] for i in range(25)]
print("Przed:", arr)
merge_sort(arr)
print("Po: ", arr)
