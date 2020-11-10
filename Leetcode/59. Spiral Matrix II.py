n = 4

emptyMatrix = [[0]*n]*n
count = 1
col_index = 0
row_index = 0
matrix = [str(i) for i in range(1,n**2+1)]
print(matrix)

while count != n**2:
    if row_index == 0:
        