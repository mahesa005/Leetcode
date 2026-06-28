class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2
            h_needed = 0
            for pile in piles:
                h_needed += (pile + mid - 1) // mid
            if h_needed > h:
                left = mid + 1
            else:
                right = mid - 1
        return left