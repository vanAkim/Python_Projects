class NumArray:

    def __init__(self, nums):
        self.nums = nums
        NumArray.update(self, 0, nums[0])

    def update(self, i: int, val: int) -> None:
        self.nums[i] = val
        A = self.nums
        SumArray = [0 for _ in A]
        for i in range(0, len(A)):
            if i == 0:
                SumArray[0] = A[0]
            else:
                SumArray[i] = A[i] + SumArray[i - 1]
        self.SumArray = SumArray

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.SumArray[j]
        else:
            return self.SumArray[j] - self.SumArray[i - 1]

objet = NumArray([1,3,5])
print(objet.sumRange(0, 2))
