class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxContainerArea = (min(height[left], height[right]) * (right - left))

        while right > left:
            if height[left] > height[right]:
                right -= 1
            else: 
                left += 1
            containerArea = (min(height[left], height[right]) * (right - left))
            maxContainerArea = max(maxContainerArea, containerArea)
        return maxContainerArea