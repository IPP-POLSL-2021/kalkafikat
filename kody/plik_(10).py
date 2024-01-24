
from random import randint

arr1 = [[randint(1, 15), randint(1, 10)] for _ in range(50)]
arr2 = [(4, 2), (2, 2), (4, 1), (5, 5), (3, 3), (4, 5)]


def split(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1


def quicksort(array: list, left=None, right=None):
    if left is None and right is None:
        left, right = 0, len(array)-1

    if left < right:
        pi = split(array, left, right)
        quicksort(array, left, pi - 1)
        quicksort(array, pi + 1, right)


print("Przed: ")
print(arr1)
quicksort(arr1)
print("Po: ")
print(arr1)
