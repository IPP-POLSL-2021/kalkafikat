source = "Pies i kot goni kota, a kot ucieka i kot"
search = "kot"

searchLength = len(search)
primeNum = 17

pomocnicza = {}
pomocnicza["a"] = 0
pomocnicza["c"] = 1
pomocnicza["e"] = 2
pomocnicza["g"] = 3
pomocnicza["i"] = 4
pomocnicza["k"] = 5
pomocnicza["n"] = 6
pomocnicza["o"] = 7
pomocnicza["P"] = 8
pomocnicza["s"] = 9
pomocnicza["t"] = 10
pomocnicza["u"] = 11
pomocnicza[" "] = 12
pomocnicza[","] = 13

counter = 0


def countValue(current):
    result = 0
    wykladnik = searchLength-1
    for x in range(0, len(current)):
        result = result + (pomocnicza[current[x]]*pow(searchLength, wykladnik))
        wykladnik -= 1
    return result % primeNum


properValue = countValue(search)

for x in range(0, len(source)):
    current = source[x:x+searchLength]
    value = countValue(current)
    if x == 0 or source[x-1] == " ":
        if x + searchLength == len(source) or source[x + searchLength] == " ":
            counter += 1

print("Słowo: " + search + " znaleziono: " + str(counter) + " razy")
