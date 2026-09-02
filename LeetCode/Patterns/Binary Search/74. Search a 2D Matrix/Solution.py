class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        low = 0
        high = rows - 1

        while low <= high:
            mid = (low + high) // 2

            if matrix[mid][cols - 1] < target:
                low = mid + 1
            else:
                high = mid - 1

        row = low

        if row == rows:
            return False

        low = 0
        high = cols - 1

        while low <= high:
            mid = (low + high) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False