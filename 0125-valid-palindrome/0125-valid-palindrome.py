class Solution:
    def isPalindrome(self, s: str) -> bool:
        input = "".join(c for c in s if c.isalnum()).lower()
        reversed = input[::-1]
        for i in range (len(input)):
            if input[i] != reversed[i]:
                return False
        return True
        