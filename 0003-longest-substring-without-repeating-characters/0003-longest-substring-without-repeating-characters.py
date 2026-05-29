class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        seen = {}
        right, left = 0, 0

        for right in range(len(s)):
            if s[right] in seen:
                left = max(left, seen[s[right]] + 1)
            seen[s[right]] = right
            longest = max(longest, right - left + 1)
        return longest