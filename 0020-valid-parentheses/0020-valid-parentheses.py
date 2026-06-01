class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for char in s:
            if char in '([{':
                stack.append(char)
            else:
                if not stack:
                    return False
                val = stack.pop()
                if char == ']' and val != '[':
                    return False
                if char == ')' and val != '(':
                    return False
                if char == '}' and val != '{':
                    return False
        return not stack