class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        input -> arrays of numbers
        what we want to do: find the next highest temperature idx from curr idx
        output -> idx of the next higher temperature from curr idx
        """
        # We use an increasing(?) monotonic stack
        n = len(temperatures)
        result = [0] * n
        s = []
        for i in range (n):
            while ((len(s)) > 0 and (temperatures[i] > temperatures[s[-1]])):
                index = s.pop()
                result[index] = i - index
            s.append(i)
        return result
        