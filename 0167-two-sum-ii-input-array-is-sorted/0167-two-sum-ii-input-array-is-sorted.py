class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
            found = False
            left = 0
            right = len(numbers) - 1

            while (found == False):
                if numbers[left] + numbers[right] == target:
                    found = True
                elif numbers[left] + numbers[right] < target:
                    left += 1
                else:
                    right -= 1                     
            return [left + 1, right + 1]