nums = [12,345,2,6,7896]
i = 0

for num in nums:
    if len(str(num))%2 == 0:
        i += 1

print(i)