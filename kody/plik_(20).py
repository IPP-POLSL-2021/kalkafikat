text="Ala przez przypadek uruchomiła alarm."
pattern="Ala"

text=input()
pattern=input()

m=len(pattern)


for i in range(len(text)-m):
    k=""
    for j in range(len(pattern)-1,-1,-1):
        if(text[i+j]!=pattern[j]):
            i+=len(pattern)-j-1
            break
        k=text[i+j]+k    
    if k == pattern:
        print("found "+ pattern)
    
print("koniec")