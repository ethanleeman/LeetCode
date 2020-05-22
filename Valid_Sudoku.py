class Solution:
    def checkRows(self, board: List[List[str]]) -> bool:
        for i in range(0,9):
            d = {}
            for j in range(0,9):
                if (board[i][j] != '.'):
                    if (d.get(board[i][j]) is not None): return False
                    d[board[i][j]] = board[i][j]
        return True

    def checkColumns(self, board: List[List[str]]) -> bool:
        for j in range(0,9):
            d = {}
            for i in range(0,9):
                if (board[i][j] != '.'):
                    if (d.get(board[i][j]) is not None): return False
                    d[board[i][j]] = board[i][j]
        return True

    def checkBoxes(self, board: List[List[str]]) -> bool:
        for i in range(0,3):
            for j in range(0,3):
                d = {}
                for i2 in range(0,3):
                    for j2 in range(0,3):
                        if (board[3*i+i2][3*j+j2] != '.'):
                            if (d.get(board[3*i+i2][3*j+j2]) is not None): return False
                            d[board[3*i+i2][3*j+j2]] = board[3*i+i2][3*j+j2]
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.checkBoxes(board) and self.checkRows(board) and self.checkColumns(board)
        
