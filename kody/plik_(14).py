# Zadanie 1

def P(t, p):
    for l in p.keys():
        if l == t:
            return p[t]
    return 0


def bayer_moore(t, x):
    t += " "
    p = {l: i for i, l in enumerate(x)}
    c = 0
    l = len(x)
    i = l - 1
    j = l - 1
    while i < len(t):
        while t[i] == x[j]:
            i -= 1
            j -= 1
            if j == -1:
                c += 1
                break
        i += l - min(j, 1 + P(t[i], p))
        j = l - 1
    return c


#text = "Pies goni kota, a kot ucieka. Kot uciekł, bo kot jest szybki"
text = "Kot goni kota i koty gonią koty. Kot uciekł, ale koty nie uciekły"
key = "kot"
key2 = "kot "

all_keys = bayer_moore(text.lower(), key)
single_keys = bayer_moore(text.lower(), key2)
print(f"Ilość słowa {key}, jako część innego słowe: {all_keys - single_keys}")

# Zadanie 2
from heapq import heappush, heappop
import random

def heap_sort(l):
    heap = []
    for e in l:
        heappush(heap, e)
    ans = [heappop(heap) for _ in range(len(heap))]
    ans.reverse()
    return ans
    
grades = []
for i in range(50):
    grades.append((random.randint(0, 10), random.randint(0, 10)))

print(heap_sort([x[0] + x[1] for x in grades]))