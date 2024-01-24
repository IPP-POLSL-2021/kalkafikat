def boyer_moore(text, pattern):
    n = len(text)
    m = len(pattern)
    i = -1
    licznik = 0
    while i < n - m:
        i += m
        if text[i] in pattern:
            for k in range(1, m + 1):
                if text[i + k - m:i + k] == pattern:
                    licznik += 1
                    i += k - 1
                    break
    print("Liczba wystąpień wzorca:",licznik)


tekst = input("Wpisz tekst: ")
wzorzec = input("Wpisz wzorzec: ")
boyer_moore(tekst, wzorzec)