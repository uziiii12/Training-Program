class Solution:
    def solveNQueens(self, n: int):
        ans = []
        board = [["."] * n for _ in range(n)]

        def backtrack(row):
            if row == n:
                result = []
                for r in board:
                    result.append("".join(r))
                ans.append(result)
                return

            for col in range(n):
                if self.isSafe(board, row, col, n):
                    board[row][col] = "Q"

                    backtrack(row + 1)

                    board[row][col] = "."

        backtrack(0)
        return ans

    def isSafe(self, board, row, col, n):

        # Check column
        for i in range(row):
            if board[i][col] == "Q":
                return False

        # Check upper-left diagonal
        i = row - 1
        j = col - 1

        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        # Check upper-right diagonal
        i = row - 1
        j = col + 1

        while i >= 0 and j < n:
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1

        return True