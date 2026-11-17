class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        len_nums1 = len(nums1)
        for i in range (m, len_nums1):
            nums1[i] = nums2[i - m]
        return nums1.sort()
        
        