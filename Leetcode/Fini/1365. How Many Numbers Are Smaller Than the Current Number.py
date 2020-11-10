
numsArray = [6,5,4,8]
numsArraySorted = sorted(numsArray)
howManySmallerNumArray = [0 for _ in numsArray]
for i in range(len(numsArray)):
    if numsArraySorted[i] == numsArraySorted[i - 1]:
        howManySmallerNumArray[i] = howManySmallerNumArray[i - 1]
    else:
        howManySmallerNumArray[i] = i

tampon = [0 for _ in numsArray]
for i in range(len(numsArray)):
    tampon[i] = howManySmallerNumArray[numsArraySorted.index(numsArray[i])]

print(tampon)