class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(rows):
            if target <= matrix[r][cols - 1]:
                low = 0
                high = cols - 1

                while low <= high:
                    mid = (low + high) // 2

                    if matrix[r][mid] == target:
                        return True
                    elif matrix[r][mid] < target:
                        low = mid + 1
                    else:
                        high = mid - 1

                return False

        return False