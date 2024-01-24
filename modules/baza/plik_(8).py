def last_occ(P, char):
    i = len(P) - 1
    for j in reversed(P):
        if (j == char):
            return i
        i -= 1
    return -1


T = "Ala przez przypadek uruchomila alarm"
P = "Ala"
n = len(T)
m = len(P)
i = 0
count = 0
while i <= n-m:
    j = m - 1
    while P[j] == T[j + i]:
        if j == 0:
            count+=1
            #print(P, j+i)
            break
        else:
            j -= 1
    j = m - 1
    i += m - min(j, 1 + last_occ(P,T[j + i]))

print("Ala: ",count)