nums = [1,2]
notCheck = True
i=1
while notCheck:
    try:
        if nums[i - 1] == nums[i]:
            nums.pop(i)
        else:
            i += 1

    except IndexError:
        notCheck = False

print(nums)
