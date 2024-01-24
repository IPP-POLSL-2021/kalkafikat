import random
arr = []
for i in range(25):
    a = random.randint(1,6)
    b = random.randint(1,6)
    arr.append([a,b])

print("Unsorted array is: ")
print(arr)

def mergeSort(arr):
    if len(arr) > 1:
        i = j = k = 0
        if len(arr) == 2:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]
            while i < len(L) and j < len(R):
                if L[i][0] < R[j][0]:
                    arr[k] = L[i]
                    i += 1
                elif L[i][0] == R[j][0]:
                    if L[i][1] < R[j][1]:
                        arr[k] = L[i]
                        i += 1
                    else:
                        arr[k] = R[j]
                        j += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
        else:        

            third = len(arr)//3
            L = arr[:third]
            M = arr[third:2*third]
            R = arr[2*third:]

            mergeSort(L)
            mergeSort(M)
            mergeSort(R)

            while i < len(L) and j < len(M) and k < len(R):
                if L[i][0] < M[j][0] and L[i][0] < R[k][0]:
                    arr[i+j+k] = L[i]
                    i += 1
                elif M[j][0] < L[i][0] and M[j][0] < R[k][0]:
                    arr[i+j+k] = M[j]
                    j += 1
                elif R[k][0] < L[i][0] and R[k][0] < M[j][0]:
                    arr[i+j+k] = R[k]
                    k += 1
                elif L[i][0] == M[j][0] and L[i][0] < R[k][0]:
                    if L[i][1] < M[j][1]:
                        arr[i+j+k] = L[i]
                        i += 1
                    else:
                        arr[i+j+k] = M[j]
                        j += 1
                elif L[i][0] == R[k][0] and L[i][0] < M[j][0]:
                    if L[i][1] < R[k][1]:
                        arr[i+j+k] = L[i]
                        i += 1
                    else:
                        arr[i+j+k] = R[k]
                        k += 1
                elif M[j][0] == R[k][0] and M[j][0] < L[i][0]:
                    if M[j][1] < R[k][1]:
                        arr[i+j+k] = M[j]
                        j += 1
                    else:
                        arr[i+j+k] = R[k]
                        k += 1
                else:
                    if L[i][1] < M[j][1] and L[i][1] < R[k][1]:
                        arr[i+j+k] = L[i]
                        i += 1
                    elif M[j][1] < L[i][1] and M[j][1] < R[k][1]:
                        arr[i+j+k] = M[j]
                        j += 1
                    else:
                        arr[i+j+k] = R[k]
                        k += 1
            while i < len(L) and j < len(M):
                if L[i][0] < M[j][0]:
                    arr[i+j+k] = L[i]
                    i += 1
                elif L[i][0] == M[j][0]:
                    if L[i][1] < M[j][1]:
                        arr[i+j+k] = L[i]
                        i += 1
                    else:
                        arr[i+j+k] = M[j]
                        j += 1
                else:
                    arr[i+j+k] = M[j]
                    j += 1
            while i < len(L) and k < len(R):
                if L[i][0] < R[k][0]:
                    arr[i+j+k] = L[i]
                    i += 1
                elif L[i][0] == R[k][0]:
                    if L[i][1] < R[k][1]:
                        arr[i+j+k] = L[i]
                        i += 1
                    else:
                        arr[i+j+k] = R[k]
                        k += 1
                else:
                    arr[i+j+k] = R[k]
                    k += 1
            while j < len(M) and k < len(R):
                if M[j][0] < R[k][0]:
                    arr[i+j+k] = M[j]
                    j += 1
                elif M[j][0] == R[k][0]:
                    if M[j][1] < R[k][1]:
                        arr[i+j+k] = M[j]
                        j += 1
                    else:
                        arr[i+j+k] = R[k]
                        k += 1
                else:
                    arr[i+j+k] = R[k]
                    k += 1
            while i < len(L):
                arr[i+j+k] = L[i]
                i += 1
            while j < len(M):
                arr[i+j+k] = M[j]
                j += 1
            while k < len(R):
                arr[i+j+k] = R[k]
                k += 1

print("Sorted array is: ")

mergeSort(arr)
print(arr)