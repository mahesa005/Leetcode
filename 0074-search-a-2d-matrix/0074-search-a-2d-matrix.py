class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, inner_left = 0, 0
        right, inner_right = len(matrix) - 1, len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            while inner_left <= inner_right:
                inner_mid = (inner_left + inner_right) // 2
                if matrix[mid][inner_mid] < target:
                    inner_left = inner_mid + 1
                elif matrix[mid][inner_mid] > target:
                    inner_right = inner_mid - 1
                else:
                    return True
            inner_left = 0
            inner_right = len(matrix[0]) - 1
            if matrix[mid][inner_left] < target:
                left = mid + 1
            elif matrix[mid][inner_left] > target:
                right = mid - 1
        return False