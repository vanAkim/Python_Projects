#["NumArray","sumRange","sumRange","sumRange"]
#[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]

nums = [-2,0,3,-5,2,-1]
i,j = [0,2]

res = 0
if i <= j:
    print(i,j)
    while j+1 > i:
        print(i)
        res = nums[i] + res
        i += 1
        print("i",i)
        print("res",res)



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)