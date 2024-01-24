#Algorytm Boyer-Moore
t = "ala ma ktakota nA OBIAD kota"
p = "kota"
n = len(t)
m = len(p)
i = 0
licznik = 0
while i<n-m+1:
    j = m-1
    while j>=0:
        if p[j] == t[i+j]:
            if j==0:
                licznik+=1
                break
            else:
                j-=1
        elif j!=m-1:
            i=i+(m-j)
            break
        else:
            break
    if not t[i+m-1] in p:
        i=i+m
    i+=1
print("Słowo", p,"pojawia się",licznik,"razy")