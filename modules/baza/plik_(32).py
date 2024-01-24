import decimal
import random

def qs(tab):
	i=0
	dl=1
	while i <len(tab[0])-1:
		if tab[0][i] == tab[0][i+1]:
			dl += 1
		else:
			t = dl
			temp = tab[1][i-t:i]
			temp.sort()

		i += 1


def quickSort(tab):
	quicksort(tab, 0, len(tab[0]) - 1)
	qs(tab)


def quicksort(tab, begin, end):
	if len(tab) > 3:
		a = random.randrange(len(tab[0]))
		b = random.randrange(len(tab[0]))
		c = random.randrange(len(tab[0]))
		tabtemp = [tab[a], tab[b], tab[c]]
		tabtemp.sort();
		pivot = tabtemp[1]
	else:
		mid = (begin + end) / 2
		mid = decimal.Decimal(mid).quantize(decimal.Decimal('1'), rounding=decimal.ROUND_HALF_UP)
		mid = int(mid)
		pivot = tab[0][mid]
	i = begin
	j = end
	while i <= j:
		while tab[0][i] < pivot:
			i += 1
		while tab[0][j] > pivot:
			j -= 1
		if i <= j:
			temp = tab[0][i]
			temp2 = tab[1][i]
			tab[0][i] = tab[0][j]
			tab[1][i] = tab[1][j]
			tab[0][j] = temp
			tab[1][j] = temp2
			i += 1
			j -= 1
	if begin < j:
		quicksort(tab, begin, j)
	if end > i:
		quicksort(tab, i, end)


table = [[0, 20, 13, 2, 13, 25, 26, 14, 15, 15, 0, 7, 0, 13, 0, 29, 20, 5, 14, 25, 21, 24, 20, 2, 7, 19, 14, 30, 1, 23],
		[29, 0, 30, 30, 10, 29, 30, 25, 9, 30, 18, 14, 10, 8, 29, 13, 0, 20, 7, 1, 29, 29, 9, 10, 14, 17, 8, 16, 7, 4]]
quickSort(table)
print(table[0])
print(table[1])
