def z1(text, find):
    pattern = {}
    limf = len(find)
    limt = len(text)
    for i in range(0, limf):
        pattern[find[i]] = max(1, limf - i - 1)
    suma = 0
    i = limf - 1
    j = 0
    while i + j < limt:
        # Napotyka taką samą literę
        if text[i + j] == find[-1]:
            same = True
            for c in range(0, limf):
                if find[limf - c - 1] != text[i + j - c]:
                    same = False
                    break
            if same:
                #print(find, i + j - limf + 1)
                suma += 1
                i += limf + j
                j = 0

        # Napotyka literę z słowa szukanego
        if text[i + j] in pattern:
            j += pattern[text[i + j]]
        else:
            i += limf
            j = 0
    return suma

#print(z1("Ala przez przypadek uruchomiła alarm", "Ala"))


import math
import random

def z2():
    ar = []
    for i in range(0, 9):
        ar.append([random.randint(1, 6), random.randint(1, 6)])
    print(ar)

    def merge(left, center, right):
        n = []

        if left is None:
            left = [[-1,-1]]
        if right is None:
            right = [[-1, -1]]
        if center is None:
            center = [[-1,-1]]

        print("l: ",left)
        print("c: ", center)
        print("r: ", right)

        # SZUKA NAJMNIEJSZEGO Z POŚRÓD 3
        while len(left) != 0 and len(center) != 0 and len(right) != 0:
            if left[0][0] == min(left[0][0], center[0][0], right[0][0]):
                n.append(left.pop(0))
            elif right[0][0] == min(left[0][0], center[0][0], right[0][0]):
                n.append(right.pop(0))
            else:
                n.append(center.pop(0))

            # JEŚLI DWA OSTATNIE [0] SĄ TAKIE SAME TO SORTUJE [1]
            if len(n) >= 2:
                print(n)

                if n[len(n) - 1][0] == n[len(n) - 2][0]:
                    if n[len(n) - 1][1] > n[len(n) - 2][1]:
                        n[len(n) - 1][1], n[len(n) - 2][1] = n[len(n) - 2][1], n[len(n) - 1][1]

        x = []
        if len(left) != 0:
            x.append(left)
        if len(center) != 0:
            x.append(center)
        if len(right) != 0:
            x.append(right)

        print("x: ",x)

        while len(x[0]) != 0 and len(x[1]) != 0:
            if x[0][0][0] < x[1][0][0]:
                n.append(x[0].pop(0))
            else:
                n.append(x[1].pop(0))
            # JEŚLI DWA OSTATNIE [0] SĄ TAKIE SAME TO SORTUJE [1]
            if len(n) >= 2:
                print(n)

                if n[len(n) - 1][0] == n[len(n) - 2][0]:
                    if n[len(n) - 1][1] > n[len(n) - 2][1]:
                        n[len(n) - 1][1], n[len(n) - 2][1] = n[len(n) - 2][1], n[len(n) - 1][1]

        if len(x[0]) == 0:
            y = x[1]
        else:
            y = x[0]

        while len(y) != 0:
            n.append(y.pop(0))
            # JEŚLI DWA OSTATNIE [0] SĄ TAKIE SAME TO SORTUJE [1]
            if len(n) >= 2:
                print(n)

                if n[len(n) - 1][0] == n[len(n) - 2][0]:
                    if n[len(n) - 1][1] > n[len(n) - 2][1]:
                        n[len(n) - 1][1], n[len(n) - 2][1] = n[len(n) - 2][1], n[len(n) - 1][1]

        print("n: ", n)
        return n

    def mergesort(l):
        lim = len(l)

        if lim <= 1:
            return l

        m = lim // 3

        print(l[:m])
        print(l[m: 2 * m])
        print(l[2 * m:])

        left = mergesort(l[:m])
        center = mergesort(l[m: 2 * m])
        right = mergesort(l[2 * m:])

        return merge(left, center, right)

    ar = mergesort(ar)
    print("ar: ", ar)

z2();
