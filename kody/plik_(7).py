def findPattern(text, pattern):
    n = len(txt)
    m = len(pattern)
    i = m-1
    j = m-1
    counter = 0
    for i in range(n-1):
        while txt[i] == pat[j]:
            i-=1
            j-=1
        if j == -1 and txt[i-len(pat):i]!= pat:
                counter+=1
                j = 0
        else:
            i+= m - min(j, 1+in_p(text[i]))
            j = m -1
           
    return counter

def in_p(letter):
    for l in p.keys():
        if l == letter:
            return p[letter]
    return -1

txt = "kota kota kot kota  "
pat = "kot"
p = {letter:index for index, letter in enumerate(pat)}
print(findPattern(txt, pat))