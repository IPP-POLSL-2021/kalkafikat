import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    if len(arr) == 2:
        if arr[0][0] < arr[1][0]:
            return arr
        elif arr[1][0] < arr[0][0]:
            return [arr[1],arr[0]]
        elif arr[0][1] < arr[1][1]:
            return arr
        elif arr[1][1] <= arr[0][1]:
            return [arr[1],arr[0]]
    piv1 = len(arr) // 3
    piv2 = (len(arr) // 3)*2
    left = arr[:piv1]
    mid = arr[piv1:piv2]
    right = arr[piv2:]
    left = merge_sort(left)
    mid = merge_sort(mid)
    right = merge_sort(right)
    return merge(left,mid, right)

def merge(left,mid, right):
    result = []
    i = j = k = 0
    while i < len(left) and j < len(right) and k < len(mid):
        if left[i][0] < right[j][0] and left[i][0] < mid[k][0]:
            result.append(left[i])
            i += 1
        elif right[j][0] < left[i][0] and right[j][0] < mid[k][0]:
            result.append(right[j])
            j += 1
        elif mid[k][0] < left[i][0] and mid[k][0] < right[j][0]:
            result.append(mid[k])
            k += 1
        elif left[i][0] == right[j][0]:
            if left[i][1] < right[j][1]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        elif left[i][0] == mid[k][0]:
            if left[i][1] < mid[k][1]:
                result.append(left[i])
                i+=1
            else:
                result.append(mid[k])
                k+=1
        elif mid[k][0] == right[j][0]:
            if mid[k][1] < right[j][1]:
                result.append(mid[k])
                k+=1
            else:
                result.append(right[j])
                j+=1
        elif left[i][1] <= right[j][1] and left[i][1] <= mid[k][1]:
            result.append(left[i])
            i += 1
        elif right[j][1] <= left[i][1] and right[j][1] <= mid[k][1]:
            result.append(right[j])
            j += 1
        elif mid[k][1] <= left[i][1] and mid[k][1] <= right[j][1]:
        # else:
            result.append(mid[k])
            k += 1
    #bład w odpowiedzi pojawia się w gdy znajduja sie 2 tablice o najmniejszym znaku wtdy zamiast wybrać tą o mneijszym drugim znaku losuje z wszystkich trzech
    if k >= len(mid):
        while i < len(left) and j < len(right):
            if left[i][0] < right[j][0]:
                result.append(left[i])
                i += 1
            elif right[j][0] < left[i][0]:
                result.append(right[j])
                j += 1
            elif left[i][1] < right[j][1]:
                result.append(left[i])
                i += 1
            elif right[j][1] <= left[i][1]:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
    elif j >= len(right):
        while k < len(mid) and i < len(left):
            if mid[k][0] < left[i][0]:
                result.append(mid[k])
                k += 1
            elif left[i][0] < mid[k][0]:
                result.append(left[i])
                i += 1
            elif mid[k][1] < left[i][1]:
                result.append(mid[k])
                k += 1
            elif left[i][1] <= mid[k][1]:
                result.append(left[i])
                i += 1
        result += mid[k:]
        result += left[i:]
    elif i >= len(left):
            while j < len(right) and k < len(mid):
                if right[j][0] < mid[k][0]:
                    result.append(right[j])
                    j += 1
                elif mid[k][0] < right[j][0]:
                    result.append(mid[k])
                    k += 1
                elif right[j][1] < mid[k][1]:
                    result.append(right[j])
                    j += 1
                elif mid[k][1] <= right[j][1]:
                    result.append(mid[k])
                    k += 1
            result += right[j:]
            result += mid[k:]
    return result

# Generate the 2-dimensional array with 25 random pairs
arr = [[random.randint(1, 6), random.randint(1, 6)] for _ in range(25)]
print("Arr:", arr)

# Sort the array by first element of each pair
arr = merge_sort(arr)
print("Posortowany:", arr)