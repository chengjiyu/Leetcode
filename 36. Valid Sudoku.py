# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
# A partially filled sudoku which is valid.
# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable.
# Only the filled cells need to be validated
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # 数独：每一行，每一列，9个9宫格里的数字只能是0-9，且不能重复
        # 记录所有出现过的行，列，块的数字及位置，判断是否有重复
        seen = []
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if j != '.':
                    seen += [(c,j),(i,c),(i/3,j/3,c)]
        return len(seen) == len(set(seen))
        # 不能用 [[False*9]*9]初始化，涉及深浅拷贝
        row = [[False for i in range(9)] for j in range(9)]
        col = [[False for i in range(9)] for j in range(9)]
        block = [[False for i in range(9)] for j in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])-1
                    k = i/3*3 + j/3
                    if row[i][num] or col[j][num] or block[k][num]:
                        return False
                    row[i][num] = col[j][num] = block[k][num] = True
                    # i,j,k表示位置，num表示出现数字，判断是否重复出现过
        return True