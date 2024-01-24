import random


def merge(left, middle, right):
    wyn = []
    i = j = k = h = 0
    while i < len(left) and j < len(middle) and k < len(right):
        if left[i][0] <= middle[j][0] and left[i][0] <= right[h][0]:
            arr[k] = left[i]
            i += 1
        elif middle[j][0] <= left[i][0] and middle[j][0] <= right[h][0]:
            arr[k] = middle[j]
            j += 1
        else:
            arr[k] = right[h]
            h += 1
    wyn += left[i:]
    wyn += middle[j:]
    wyn += right[h:]
    return wyn


def merge_sort(tab):
    if len(tab) > 1:
        m = len(tab) // 3
        left = merge_sort(tab[:m])
        middle = merge_sort(tab[m:m])
        right = merge_sort(tab[m:])
        return merge(left, middle, right)


def sort_pairs(arr):
    merge_sort(arr)
    for i in range(len(arr)):
        if i > 0 and arr[i][0] == arr[i-1][0]:
            if arr[i][1] < arr[i-1][1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
    return arr


arr = [[random.randint(1, 6), random.randint(1, 6)] for i in range(25)]
print("Przed: ", arr)
merge_sort(arr)
print("Po: ", arr)
