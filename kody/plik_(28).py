def search(text, pattern):
    m = len(pattern)
    n = len(text)
    i = m-1
    j = m-1
    ile_jest = 0
    counter = 0
    while i < n and i > -2:
        temp = i
        while text[i] == pattern[j]:
            i-=1
            j-=1
            if j == -1: break
        i = temp
        if j == -1:
            counter += 1
            i = m - 1 + m * counter
            ile_jest += 1
        else:
            if text[i] in pattern:
                i+=1
            else:
                counter +=1
                i = m-1 + m*counter
        j = m - 1
    return ile_jest
text = "Ala przez przypadek Ala uruchomila alarm. Ala"
pattern = "Ala"
print("Wzorzec powtarza sie nastepujaca ilosc razy: "+str(search(text, pattern)))



