def karp_rabin():
    print("Podaj tekst: ")
    t = input()
    print("Podaj wzorzec: ")
    p = input()
    n = len(t)
    m = len(p)
    h1 = 1
    h2 = 1
    r = 256 #liczba symboli alfabetu (char 0-255)
    q = 29 #liczba pierwsza
    wynik = 0
    for i in range(m):
        h1 = ((h1*r)+ord(p[i]))
        h1 = h1%q
    for i in range(n-m):
        h2 = 1
        for j in range(m):
            h2 = ((h2 * r) + ord(t[i+j]))
            h2 = h2 % q
        if(h1==h2):
            if(p[:]==(t[i:i+m])):
                wynik += 1
    return wynik
print(karp_rabin())
