def karprabin(T, P):
    dlugosc_alfabetu = 256
    prime = 11
    n = len(T)
    m = len(P)
    h = pow(dlugosc_alfabetu, m - 1)
    t_hash = 0
    p_hash = 0
    j = 0
    licznik = 0
    for _ in range(m):
        p_hash = (dlugosc_alfabetu * p_hash + ord(P[_])) % prime
        t_hash = (dlugosc_alfabetu * t_hash + ord(T[_])) % prime

    for i in range(n - m):
        if t_hash == p_hash:
            for j in range(m):
                if T[i + j] != P[j]:
                    break
                else:
                    j += 1
            if j == m:
                if T[i-1] == " " and (T[i + len(P)] == " " or T[i + len(P)] == "."):
                    licznik += 1
                    print(f"Wzorzec '{P}' na pozycji {i}")
        t_hash = (dlugosc_alfabetu * (t_hash - ord(T[i]) * h) + ord(T[i + m])) % prime
    print(f"Ilosc wystapen: {licznik}")


if __name__ == '__main__':
    wzorzec = "kot"
    karprabin("Pies gonikota kota, a kot kot ucieka kot.",
              wzorzec)
