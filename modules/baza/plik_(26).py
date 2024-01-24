def boyerMoore(txt, pat):
    n = len(txt)
    m = len(pat)
    i = -1
    licznik = 0
    while i < n - m:
        i += m
        if txt[i] in pat:
            for k in range(1, m + 1):
                if txt[i + k - m:i + k] == pat:
                    licznik += 1
                    i += k - 1
                    break
    print("Ilość wystąpień:",licznik)
tekst = 'ala ma kota a kot ma ale o imieniu ala'
wzorzec = 'ala'
boyerMoore(tekst,wzorzec)