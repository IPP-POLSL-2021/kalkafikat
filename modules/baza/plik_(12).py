def zad1_boyer_moore(txt, w):
    ilosc = 0
    alf = {}
    for i in range(len(w)):
        alf[w[i]] = i
    nie_litery = [' ', ',', '.']
    for i in range(len(w) - 1, len(txt), 1):
        znaleziono = True
        for j in range(0, len(w), 1):
            if w[len(w) - 1 - j].lower() != txt[i - j].lower():
                znaleziono = False
                ix = alf.get(txt[i - j].lower())
                if ix is None:
                    ix = len(w)
                i += ix
                break
        if znaleziono:
            przed = False
            za = False
            for znak in nie_litery:
                if i-len(w) > -1 and not przed:
                    if txt[i - len(w)] == znak:
                        przed = True
                if i+1 < len(txt) and not za:
                    if txt[i + 1] == znak:
                        za = True
            if not przed or not za:
                ilosc += 1
    print("Tekst: " + txt + "\nWyraz: " + w + "\nIlość: " + str(ilosc))


def zad2_second_sort(tab):
    i = 0
    dl = 0
    while i < len(tab[0]) - 1:
        if tab[0][i] == tab[0][i + 1]:
            dl += 1
        else:
            t = dl
            temp = tab[1][i - t:i + 1]
            temp.sort()
            for te in range(len(temp)):
                tab[1][i - t + te] = temp[te]
            dl = 0
        i += 1


def zad2_kopiec(last, start, end):
    root = start
    while True:
        d = root * 2 + 1
        if d > end:
            break
        if d + 1 <= end and last[d] < last[d + 1]:
            d += 1
        if last[root] < last[d]:
            help1 = last[root]
            last[root] = last[d]
            last[d] = help1
            root = d
        else:
            break


def zad2_sortowanie_kopcem(to_sort_list):
    for start in range(int((len(to_sort_list[0]) - 2) / 2), -1, -1):
        zad2_kopiec(to_sort_list[0], start, len(to_sort_list[0]) - 1)

    for end in range(len(to_sort_list[0]) - 1, 0, -1):
        help1 = to_sort_list[0][end]
        help2 = to_sort_list[1][end]
        to_sort_list[0][end] = to_sort_list[0][0]
        to_sort_list[1][end] = to_sort_list[1][0]
        to_sort_list[0][0] = help1
        to_sort_list[1][0] = help2
        zad2_kopiec(to_sort_list[0], 0, end - 1)
    return to_sort_list


def zad2_kopcowanie(tab):
    zad2_sortowanie_kopcem(tab)
    zad2_second_sort(tab)


def zad1():
    print("\nZadanie1: ")
    tekst = 'Pies goni kota, a kot ucieka. Kot uciekł, bo kot jest szybki'
    wyraz = 'kot'
    zad1_boyer_moore(tekst, wyraz)


def zad2():
    print("\nZadanie2: ")
    table = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    f = open("zad2_plik1.txt")
    g = 0
    while g < 50:
        helper = f.readline()
        table[0][g] = int(helper[1])
        table[1][g] = int(helper[4])
        g += 1
    f.close()
    zad2_kopcowanie(table)
    tabb = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    h = 0
    while h < len(table[0]):
        helper2 = '(' + str(table[0][h]) + ", " + str(table[1][h]) + ')'
        print(helper2)
        tabb[h] = helper2
        h += 1
    linia = "\n".join(tabb)
    f = open("zad2_plik2.txt", mode='w')
    f.write(linia)
    f.close()


zad1()
zad2()
