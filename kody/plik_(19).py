def quick_sort(tab, lewo, prawo):
    i = lewo
    j = prawo
    x = [tab[prawo-2],tab[prawo-1],tab[prawo]]
    pivot = x[1]
    while(True):
        while (tab[i][0] < pivot[0]):
            i+=1
        while (pivot[0] < tab[j][0]):
            j-=1
        if(pivot[0]==tab[i][0]):
            while(tab[i][1] < pivot[1]):
                i+=1
        if (pivot[0] == tab[j][0]):
            while (tab[j][1] > pivot[1]):
                j -= 1
        if (i <= j):
            temp = tab[i];
            tab[i] = tab[j];
            tab[j] = temp;
            i += 1
            j -= 1
        else:
            break
    if(lewo < j): quick_sort(tab, lewo, j)
    if(i < prawo): quick_sort(tab, i, prawo)
zad1 = []
tab = []
f = open("wyniki.txt")

for dane in f:
    zad1.append(dane)
    dane = dane[1:len(dane)-2]
    x = dane.split(",")

    z1 = int(x[0])
    z2 = int(x[1])
    tab.append([z1,z2])

quick_sort(tab,0,len(tab)-1)
print(tab)
f2 = open("sortowane.txt",mode="w")
for i in range(len(tab)):
    f2.write("("+str(tab[i][0])+","+str(tab[i][1])+")\n")
f2.close()