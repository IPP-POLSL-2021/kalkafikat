# Zadanie 1
def BoyerMoore(T, P):
    n = len(T)
    m = len(P)
    i = -1
    licznik=0
    while i < n - m:
        i += m
        if T[i] in P:
            for k in range(1, m + 1):
                if T[i + k - m:i + k] == P:
                    licznik+=1
                    i += k - 1
                    break
    print("Liczba wystąpień wzorca:",licznik)
tekst=input("Podaj tekst: ")
wzorzec=input("Podaj wzorzec: ")
BoyerMoore(tekst,wzorzec)

