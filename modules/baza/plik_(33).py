def boyerMoor(wzorzec, tekst):
    print("Boyer Moor")
    wzorzec = " "+wzorzec+" "
    znaleziono = []
    len(znaleziono)
    i = len(wzorzec) - 1
    war1 = False
    t = i
    while t < len(tekst):
        wz = wzorzec[i].lower()
        te = tekst[t].lower()
        if wz == te:
            war1 = True
            for lt in range(len(wzorzec)):

                wz = wzorzec[i - lt].lower()
                te = tekst[t - lt].lower()
                if wz != te:
                    war1 = False
                    t += 1
                    break
        else:
            tek = tekst[t].lower()
            wzor = wzorzec.lower()
            if tek not in wzor:
                if len(wzorzec) > 1:
                    t += len(wzorzec) - 1
                else:
                    t += 1
            else:
                for w in range(len(wzorzec)):
                    if tek == wzor[w]:
                        t += len(wzorzec) - w - 1
                        break
        if war1:
            war1 = False
            znaleziono.append(t - len(wzorzec) + 1)
            t += 1
    wzorzec=wzorzec.strip(" ")
    if len(znaleziono) != 0:
        return f" w tekscie \"{tekst}\" znaleziono wzorzec \"{wzorzec}\" {len(znaleziono)} razy na miejscach {znaleziono} "
    else:
        return f"nie znaleziono wzorca w tekscie"


def main():
    tekst = "pies goni kota, a kot ucieka, pies nie może złapać Kota, więc Kot uciekł, kot się cieszy";
    wzorzec = "kot"
    print(boyerMoor(wzorzec, tekst))


if __name__ == "__main__":
    main()
