#zad 1 (KOLOS) - algorytm Boyera - Moore'a

import sys


def BoyerMoore(text, key):
    n = len(text)
    m = len(key)
    if m == 0:
        return n
    tab = [-1] * 256
    for i in range(m):
        tab[ord(key[i])] = i
    i = 0
    wystapienie = 0
    while i < n - m + 1:
        j = m - 1
        while j >= 0 and key[j] == text[i + j]:
            j -= 1
        if j == -1:
            wystapienie += 1
            i += m
        else:
            i += max(1, j - tab[ord(text[i + j])])
    return wystapienie

# text = "Ala przez przypadek uruchomiaa alarm"
# text2 = "Ala ma Ala"
# key = "Ala"


text = sys.argv[1]
key = sys.argv[2]

print("Liczba wystapien zadanego slowa: ", BoyerMoore(text, key))
