class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for list in accounts:
            if sum(list) >= max:
                max = sum(list)
        return max
            
            