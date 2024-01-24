import random
tab = []
for i in range(25):
    tab.append([random.randint(1,6), random.randint(1,6)])

def split(arr, idx):
    if len(arr)==1 or len(arr)==0:
        return arr
    L = split(arr[:len(arr)//3], idx)
    C = split(arr[len(arr)//3:2*len(arr)//3], idx)
    R = split(arr[2*len(arr)//3:], idx)
    i, j, k = 0, 0, 0
    tmp = []
    while(i<len(L) and j<len(C) and k<len(R)):
        if L[i][idx] <= C[j][idx] and L[i][idx] <= R[k][idx]:
            tmp.append(L[i])
            i += 1
        elif C[j][idx] <= L[i][idx] and C[j][idx] <= R[k][idx]:
            tmp.append(C[j])
            j += 1
        else:
            tmp.append(R[k])
            k += 1
    if i == len(L):
        while(j<len(C) and k<len(R)):
            if C[j][idx] <= R[k][idx]:
                tmp.append(C[j])
                j += 1
            else:
                tmp.append(R[k])
                k += 1
        if j == len(C):
            while(k<len(R)):
                tmp.append(R[k])
                k += 1
        else:
            while(j<len(C)):
                tmp.append(C[j])
                j += 1
    elif j == len(C):
        while(i<len(L) and k<len(R)):
            if L[i][idx] <= R[k][idx]:
                tmp.append(L[i])
                i += 1
            else:
                tmp.append(R[k])
                k += 1
        if i == len(L):
            while(k<len(R)):
                tmp.append(R[k])
                k += 1
        else:
            while(i<len(L)):
                tmp.append(L[i])
                i += 1
    else:
        while(i<len(L) and j<len(C)):
            if L[i][idx] <= C[j][idx]:
                tmp.append(L[i])
                i += 1
            else:
                tmp.append(C[j])
                j += 1
        if i == len(L):
            while(j<len(C)):
                tmp.append(C[j])
                j += 1
        else:
            while(i<len(L)):
                tmp.append(L[i])
                i += 1
    return tmp

arr = split(tab, 0)

arr1 = [i for i in arr if i[0] == 1]
arr1 = split(arr1, 1)
arr2 = [i for i in arr if i[0] == 2]
arr2 = split(arr2, 1)
arr3 = [i for i in arr if i[0] == 3]
arr3 = split(arr3, 1)
arr4 = [i for i in arr if i[0] == 4]
arr4 = split(arr4, 1)
arr5 = [i for i in arr if i[0] == 5]
arr5 = split(arr5, 1)
arr6 = [i for i in arr if i[0] == 6]
arr6 = split(arr6, 1)
sortedArr = arr1 + arr2 + arr3 + arr4 + arr5 + arr6
print(sortedArr)

