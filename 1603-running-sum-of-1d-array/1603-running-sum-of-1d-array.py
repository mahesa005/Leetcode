class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        length = len(nums) - 1
        for i in range(length, -1, -1):
            if i != 0:
                for j in range(i-1, -1, -1):
                    nums[i] += nums[j]
        return nums