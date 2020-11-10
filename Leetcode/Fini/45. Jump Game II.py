class Solution:
    def __init__(self,nums):
        self.nums = nums
    def jump(self):
        nums = self.nums
        index = 0
        count = 1
        maxJumpList = [(nums[i] + i) for i in range(len(nums))]
        print(maxJumpList)
        while nums[index] < len(nums[index+1:]):
            print("Avant : ", index, count)
            count += 1
            index = maxJumpList.index(max(maxJumpList[index+1 : index + nums[index]+1]))
            print("Après : ",index, count,"\n")
        return count
print(Solution([1,2,3]).jump())