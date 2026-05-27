class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_sequence = 0
        curr_sequence = 0
        prev = None
        nums.sort()
        print(nums)
        for i in range (len(nums)):
            if (prev is not None) and nums[i] == (prev + 1):
                curr_sequence += 1
            elif prev == nums[i]:
                print("pass")
            else:
                longest_sequence = max(longest_sequence, curr_sequence)
                curr_sequence = 0
            prev = nums[i] 
        longest_sequence = max(longest_sequence, curr_sequence)
        if len(nums) == 0:
            return 0
        return longest_sequence + 1
