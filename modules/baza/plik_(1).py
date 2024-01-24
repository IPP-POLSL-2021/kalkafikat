from random import randint


def quick_sort(tablica, lower, higher):
    if lower < higher:
        counter = 0
        piv = tablica[higher]
        for i in range(1, 3):
            if tablica[higher - i][0] >= piv[0]:
                if tablica[higher - i][0] == piv[0]:
                    counter += 1
                piv = tablica[higher - i]
        if counter > 1:
            for i in range(1, 3):
                if tablica[higher - i][1] > piv[1] and tablica[higher - i][0] == piv[0]:
                    piv = tablica[higher - i]
        index = lower - 1
        for j in range(lower, higher):
            if tablica[j][0] == piv[0] and tablica[j][1] < piv[1]:
                index = index + 1
                temp = tablica[index]
                tablica[index] = tablica[j]
                tablica[j] = temp
            elif tablica[j][0] < piv[0]:
                index = index + 1
                temp = tablica[index]
                tablica[index] = tablica[j]
                tablica[j] = temp
        index += 1
        temp = tablica[index]
        tablica[index] = tablica[higher]
        tablica[higher] = temp
        quick_sort(tablica, lower, index - 1)
        quick_sort(tablica, index, higher)


def main():
    tablica = []
    for i in range(50):
        tablica.append([randint(1, 5) for i in range(2)])
    print(f"Przed:\n {tablica}")
    quick_sort(tablica, 0, len(tablica) - 1)
    print(f"Po:\n {tablica}")


if __name__ == "__main__":
    main()
