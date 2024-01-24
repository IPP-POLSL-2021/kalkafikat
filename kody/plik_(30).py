def last_occ(P, char):
    i = len(P) - 1
    for j in reversed(P):
        if (j == char):
            return i
        i -= 1
    return -1


T = input("Podaj tekst: ")
P = input("Podaj wzorzec: ")
n = len(T)
m = len(P)
i = 0
cout = 0
while i <= n-m:
    j = m - 1
    while P[j] == T[j + i]:
        if j == 0:
            cout += 1
            break
        else:
            j -= 1
    j = m - 1
    i += m - min(j, 1 + last_occ(P,T[j + i]))
print(cout)