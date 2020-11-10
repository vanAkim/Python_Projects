

n = 7

initialSolution = []
i=0
if n%2 == 1:
    initialSolution.append(0)
    n -= 1
while i < n:
    initialSolution.append(i+1)
    initialSolution.append((i+1)*-1)
    i += 2

print(initialSolution)