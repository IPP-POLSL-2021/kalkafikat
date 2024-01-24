def boyer_moore(tekst, wzorzec):
    n = len(tekst)
    m = len(wzorzec)
    i = m - 1
    j = m - 1
    licznik = 0
    while i < n:
        if tekst[i] == wzorzec[j]:
            if j == 0:
                licznik += 1
                i = i + m
                j = m - 1
            else:
                i -= 1
                j -= 1
        else:
            lo = -1
            for k in range(m - 1):
                if wzorzec[k] == tekst[i]:
                    lo = k
            i += m - min(j, lo + 1)
            j = m - 1
    return licznik

tekst = input("Podaj tekst: ")
wzorzec = input("Podaj wzorzec: ")
print(boyer_moore(tekst, wzorzec))

