class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        mark = [[matrix[r][c] for c in range(n)] for r in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    for col in range(n):
                        mark[i][col] = 0
                    for row in range(m):
                        mark[row][j] = 0
        for r in range(m):
            for c in range(n):
                matrix[r][c] = mark[r][c]

        