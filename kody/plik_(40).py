from collections import defaultdict


def bm(t, p):
    last = defaultdict(lambda: -1)
    for x in set(p):
        last[x] = p.rfind(x)

    n = len(t)
    m = len(p)
    i = m - 1
    j = m - 1
    while(i < n):
        if(p[j] == t[i]):
            if(j == 0):
                return i + 1
            else:
                j -= 1
                i -= 1
        else:
            i += m - min(j, 1 + last[t[i]])
            j = m-1
    return -1


# T = input("Podaj tekst: ")
# P = input("Podaj wzorzec: ")
T = "Ala przez przypadek uruchomiaa alarm."
P = "Ala"

wynik = bm(T, P)

if wynik == -1:
    print("Nie znaleziono wzorca")
else:
    print(f'Znaleziono wzorzec na pozycji {wynik}')
