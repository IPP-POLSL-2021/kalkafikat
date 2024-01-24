# dlugosc alfabetu
def alphlength(_text):
    found = []
    for i in range(len(_text)):
        if _text[i] not in found:
            found.append(_text[i])
    return len(found)


def karp(TEXT, PATTERN, Q=101):
    PATTLEN = len(PATTERN)
    TEXT = TEXT.lower()
    PATTERN = PATTERN.lower();
    def fhash(_alphlen, _text):
        h = 0
        for i in range(PATTLEN):
            h += ord(_text[i]) * (_alphlen ** (PATTLEN - 1 - i))
        return h % Q

    def fhashprev(_alphlen, _prevval, _unusedchar, _addchar):
        h = (_prevval - ord(_unusedchar) * (_alphlen ** (PATTLEN - 1))) * _alphlen + ord(_addchar)
        return h % Q

    alen = alphlength(TEXT)
    hpattern = fhash(alen, PATTERN)
    i = 0
    h = 0
    repeats = []

    while i <= len(TEXT) - PATTLEN:
        if i == 0:
            h = fhash(alen, TEXT[i:i + PATTLEN])
        else:
            h = fhashprev(alen, h, TEXT[i - 1], TEXT[i + PATTLEN - 1])
        if h == hpattern:
            correct = True
            for j in range(PATTLEN):
                if TEXT[i + j] != PATTERN[j]:
                    correct = False
                    break
            if correct is True and TEXT[i + PATTLEN].isalpha() != True:
                repeats.append(i)
        i += 1

    print(f"Podtekst {PATTERN} występuje w podanym tekście {len(repeats)}.")

def main():
   karp("Pies goni kota, a kot ucieka.", "kot")
   karp("Kot kota kota goni kot kota", "kot")
   karp("Ile okno oknom zmienia życie tak okno jest oknowate okno.", "okno")
   karp("Mateusz Mateuszowi szukał Mateusza, ale Mateusz to Mateuszowaty Mateusz.", "Mateusz")


if __name__ == '__main__':
    main()