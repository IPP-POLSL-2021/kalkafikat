from heapq import heappop, heappush
import random
def heapSort(tab):
    heap = []
    heap2 = []
    wynik = []
    for value in tab:
        for element in value:
            heappush(heap, element)
        wynik.append([heappop(heap) for i in range(len(heap))])
    return wynik

 
tab = [[random.randint(0,10) for i in range(50)], [random.randint(0,10) for i in range(50)]]
print("Przed sortowaniem:")
print(tab)
tab = heapSort(tab)
print("Po:")
print(tab)