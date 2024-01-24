import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

arr = [[random.randint(1, 6), random.randint(1, 6)] for _ in range(25)]

def reverseInside(arr):
    reverArr = []
    for i in range(25):
        arrx = []
        arrx.append(arr[i][1])
        arrx.append(arr[i][0])
        reverArr.append(arrx)
    return reverArr

print(arr)
newArr = reverseInside(arr)
print(newArr)
print(merge_sort(arr))
finalArr = merge_sort(newArr)
print(finalArr)
print(reverseInside(finalArr))




