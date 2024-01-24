import random

def mergesort(lst):
    if len(lst) >= 3:
        third = len(lst) // 3
        left = mergesort(lst[:third])
        middle = mergesort(lst[third:-third])
        right = mergesort(lst[-third:])

        print(left)
        print(middle)
        print(right)

        mergesort(left)
        mergesort(middle)
        mergesort(right)

        result = []
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(middle) and k < len(right):
            if left[i] <= middle[j] and left[i] <= right[k]:
                result.append(left[i])
                i += 1
            elif middle[j] <= left[i] and middle[j] <= right[k]:
                result.append(middle[j])
                j += 1
            else:
                result.append(right[k])
                k += 1

        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(middle):
            result.append(middle[j])
            j += 1
        while k < len(right):
            result.append(right[k])
            k += 1

        return result

    else:
        return lst


if __name__ == "__main__":

    rows = 25
    columns = 2

    table = [[random.randint(0, 6) for i in range(columns)] for j in range(rows)]
    print("Unsorted array: ", table)
    print("Sorted array: ", mergesort(table))
