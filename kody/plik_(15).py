import math


def karp_rabin(source, pattern):
    count = 0
    for i in range(0, len(source) - len(pattern)):
        for j in range(0, len(pattern)):
            if source[i + j] != pattern[j]:
                break
        else:
            if source[i+len(pattern)] == " " and source[i-1] == " ":
                # print(i)
                count += 1
            # else:
            #     print("bad: ", i)
    return count

def zad1():
    text = "Piec goni kota, a kot ucieki"
    pattern = "kot"
    print("tekst: ", text, "\npattern: ", pattern)
    print("liczba wystąpień: ", karp_rabin(text, pattern))
    print("")
    text = "Pani Ala ma kota. kot je mysz, kot pije mleko i kot jest leniwy"
    pattern = "kot"
    print("tekst: ", text, "\n pattern: ", pattern)
    print("liczba wystąpień: ", karp_rabin(text, pattern))

class para:
    def __init__(self, z1, z2):
        self.z1 = z1
        self.z2 = z2
    def __repr__(self):
        return f"<para {self.z1} {self.z2}>"


def quicksort(arr, start , stop, kryterium):
	if(start < stop):
		pivotindex = partitionMiddle(arr, start, stop, kryterium)
		quicksort(arr , start , pivotindex-1, kryterium)
		quicksort(arr, pivotindex + 1, stop, kryterium)

def partitionMiddle(arr , start, stop, kryterium):
	midpivot = math.floor((start + stop) / 2)
	arr[start], arr[midpivot] = arr[midpivot], arr[start]
	return partition(arr, start, stop, kryterium)

def partition(arr,start,stop, kryterium):
	pivot = start
	i = start + 1
	
	for j in range(start + 1, stop + 1):
		if kryterium == 1:
			if arr[j].z1 <= arr[pivot].z1:
				arr[i] , arr[j] = arr[j] , arr[i]
				i = i + 1
		else:
			if arr[j].z2 <= arr[pivot].z2:
				arr[i] , arr[j] = arr[j] , arr[i]
				i = i + 1

	arr[pivot] , arr[i - 1] = arr[i - 1] , arr[pivot]
	pivot = i - 1
	return (pivot)

import random
def zad2():
    print("kryterium: ", 1)
    arr = []
    for i in range(0, 50):
        arr.append(para(random.randrange(1, 50), random.randrange(1, 50)))
    # arr = [obj1, obj2]
    print(arr)
    print("")
    quicksort(arr, 0, len(arr)-1, 1)
    print(arr)

zad2()
# zad1()
