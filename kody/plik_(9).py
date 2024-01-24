import random

def merge(gArray, low, mid1, mid2, high, destArray):
    i = low
    j = mid1
    k = mid2
    l = low
 

    while ((i < mid1) and (j < mid2) and (k < high)):
        if(gArray[i] < gArray[j]):
            if(gArray[i] < gArray[k]):
                destArray[l] = gArray[i]
                l += 1
                i += 1
            else:
                destArray[l] = gArray[k]
                l += 1
                k += 1
        else:
            if(gArray[j] < gArray[k]):
                destArray[l] = gArray[j]
                l += 1
                j += 1
                gArray[j] < gArray[k]
            else:
                destArray[l] = gArray[k]
                l += 1
                k += 1
 

    while ((i < mid1) and (j < mid2)):
        if(gArray[i] < gArray[j]):
            destArray[l] = gArray[i]
            l += 1
            i += 1
        else:
            destArray[l] = gArray[j]
            l += 1
            j += 1
 
  
    while ((j < mid2) and (k < high)):
        if(gArray[j] < gArray[k]):
            destArray[l] = gArray[j]
            l += 1
            j += 1
        else:
            destArray[l] = gArray[k]
            l += 1
            k += 1
 
  
    while ((i < mid1) and (k < high)):
        if(gArray[i] < gArray[k]):
            destArray[l] = gArray[i]
            l += 1
            i += 1
        else:
            destArray[l] = gArray[k]
            l += 1
            k += 1

    while (i < mid1):
        destArray[l] = gArray[i]
        l += 1
        i += 1

    while (j < mid2):
        destArray[l] = gArray[j]
        l += 1
        j += 1

    while (k < high):
        destArray[l] = gArray[k]
        l += 1
        k += 1
 
 
def merge3Sort(gArray, low, high, destArray):
 
    if (high - low < 2):
        return
 
   
    mid1 = low + ((high - low) // 3)
    mid2 = low + 2 * ((high - low) // 3) + 1
 
    
    merge3Sort(destArray, low, mid1, gArray)
    merge3Sort(destArray, mid1, mid2, gArray)
    merge3Sort(destArray, mid2, high, gArray)
 
    
    merge(destArray, low, mid1, mid2, high, gArray)
 
 
def mergeSort3Way(gArray, n):

    if (n == 0):
        return
 
   
    fArray = []
 
 
    fArray = gArray.copy()
 

    merge3Sort(fArray, 0, n, gArray)
 
    gArray = fArray.copy()
 

    return gArray
 
 
da = []
dan = []
dat = [[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None],[None,None]]
data=[None]*25
datb=[None]*25

for idx,x in enumerate(dat):
    x[0]=random.randrange(0,6)
    x[1]=random.randrange(0,6)
    data[idx]=x[0]
    datb[idx]=x[1]
    
   # print(idx)
    
    
    
print(dat)
print("@@@@@@@@@@@@@@@@@@@")
#print(data)
#print(datb)
 


data = mergeSort3Way(data, len(data))
#print("After 3 way merge sort: ", end="")


for x in data:
    for y in dat:
        if x==y[0]:
            da.append([x,y[1]])
            break
            
            
datb = mergeSort3Way(datb, len(datb))
#print("After 3 way merge sort: ", end="")
t=False
for y in da:
    for x in datb:
        if x==y[1]:
            dan.append([y[0],x])
            break
            
    
        


"""for i in range(len(data)):
    print(f"{data[i]} ", end="")
    
for i in range(len(datb)):
    print(f"{datb[i]} ", end="")
    
      
      """



    
print(dan)