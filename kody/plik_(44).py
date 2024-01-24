import random

def quicksort_three(arr):
    if len(arr) <= 1:
        return arr
    pivot = findpivot(arr)
    left = []
    for el in arr:
        if el < pivot:
            left.append(el)
        elif el[0] == pivot[0] and el[1] < pivot[1]:
            left.append(el)

        middle = []
        for el in arr:
            if el == pivot:
                middle.append(el)

        right = []
        for el in arr:
            if el > pivot:
                right.append(el)
            elif el[0] == pivot[0] and el[1] > pivot[1]:
                right.append(el)
    return quicksort_three(left) + middle + quicksort_three(right)


def findpivot(arr):
    first = arr[0]
    last = arr[-1]
    middle = arr[len(arr) // 2]
    median = sorted([first, last, middle])[1]
    return median


def main():
    tab = []
    for i in range(50):
        tab.append((random.randint(0, 10), random.randint(0, 10)))
    print("Przed: \n")
    print(tab)
    print("\nPo: \n")
    print(quicksort_three(tab))


if __name__ == "__main__":
    main()
