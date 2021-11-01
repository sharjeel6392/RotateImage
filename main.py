class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix[0])
        for i in range(N // 2):
            for j in range(i, N - i - 1):
                temp = matrix[i][j]
                matrix[i][j] = matrix[N - 1 - j][i]
                matrix[N - 1 - j][i] = matrix[N - 1 - i][N - 1 - j]
                matrix[N - 1 - i][N - 1 - j] = matrix[j][N - 1 - i]
                matrix[j][N - 1 - i] = temp
