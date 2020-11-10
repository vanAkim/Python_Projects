nums = [1,2,3,4]

solution = []
index = 1
while index <= len(nums)-1:
    solution += [nums[index]]*nums[index-1]
    index += 2

print(solution)
