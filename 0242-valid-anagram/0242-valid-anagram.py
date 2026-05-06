class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_tracker = {}
        for i in range (len(s)):
            if s[i] in anagram_tracker:
                anagram_tracker[s[i]] += 1
            else:
                anagram_tracker[s[i]] = 1
        
        if len(s) != len(t):
            return False
            
        for i in range (len(t)):
            if t[i] in anagram_tracker:
                if anagram_tracker[t[i]] == 0:
                    return False
                else:
                    anagram_tracker[t[i]] -= 1
            else:
                return False
        return True