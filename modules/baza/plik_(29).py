import random

def mergeSort(list):
    if len(list) > 2:
        one = len(list) // 3
        two = len(list)*2 // 3
        L = list[:one]
        M = list[one:two]
        R = list[two:]
        mergeSort(L)
        mergeSort(M)
        mergeSort(R)
        merge(list, L, R, M)
    if len(list) > 1:
        mid = len(list) // 2
        L = list[:mid]
        R = list[mid:]
        mergeSort(L)
        mergeSort(R)
        merge2(list, L, R)
def merge2(list, L, R):
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            list[k] = L[i]
            i += 1
        else:
            list[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        list[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        list[k] = R[j]
        j += 1
        k += 1
def merge(list, L, R, M):
    i = j = k = l = 0
    while i < len(L) and j < len(R) and l < len(M):
        if L[i] < R[j] and L[i] < M[l]:
            list[k] = L[i]
            i += 1
        elif R[j] < L[i] and R[j] < M[l]:
            list[k] = R[j]
            j += 1
        elif M[l] < L[i] and M[l] < R[j]:
            list[k] = M[l]
            l += 1
        elif M[l] == R[j]:
            list[k] = M[l]
            k += 1
            list[k] = R[j]
            l+=1
            j+=1
        elif M[l] == L[i]:
            list[k] = M[l]
            k += 1
            list[k] = L[i]
            l+=1
            i+=1
        elif R[j] == L[i]:
            list[k] = R[j]
            k += 1
            list[k] = L[i]
            j+=1
            i+=1
        k += 1
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            list[k] = L[i]
            i += 1
        else:
            list[k] = R[j]
            j += 1
        k += 1
    while l < len(M) and j < len(R):
        if M[l] < R[j]:
            list[k] = M[l]
            l += 1
        else:
            list[k] = R[j]
            j += 1
        k += 1
    while l < len(M) and i < len(L):
        if L[i] < M[l]:
            list[k] = L[i]
            i += 1
        else:
            list[k] = M[l]
            l += 1
        k += 1
    while i < len(L):
        list[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        list[k] = R[j]
        j += 1
        k += 1
    while l < len(M):
        list[k] = M[l]
        l += 1
        k += 1
lista = [[2,5],[4,1],[7,2],[6,4],[8,9],[1,2],[1,4],[1,1],[1,0],[8,13],[4, 1]]
list = []
n = 25
for i in range(n):
    list.append([random.randint(0, 9),random.randint(0, 9)])
mergeSort(list)
print(list)