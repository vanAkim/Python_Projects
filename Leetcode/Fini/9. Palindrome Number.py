import math


N = 10201000
i=0
Nlist = [0]*(int(math.log10(N))+1)
expo = int(math.log10(N))
while N!=0:
    if expo != int(math.log10(N)):
        i = expo - int(math.log10(N))
        Nlist[i] = math.floor(N / 10**int(math.log10(N)))
        N = N - Nlist[i]*10**int(math.log10(N))
    else:
        expo = int(math.log10(N))
        Nlist[i] = math.floor(N / 10**int(math.log10(N)))
        N = N - Nlist[i]*10**int(math.log10(N))
        i += 1

i=0
j=len(Nlist)-1
Condi = True
while Condi:
    print(Nlist,i,j,Nlist[i],Nlist[j])
    if Nlist[i] != Nlist[j]:
        Condi = False
    elif i == j or i+1==j:
        break
    else:
        i += 1
        j -= 1
        Condi = True

print("\n",Condi)