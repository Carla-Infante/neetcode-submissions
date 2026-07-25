class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        square = defaultdict(set)  #indexes of big squares from 0-2 so (r // 3, c // 3) is key 


        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or   #if the number at board[r][c] is in the dict rows
                    board[r][c] in cols[c] or
                    board[r][c] in square[r//3, c//3]):
                    return False 
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                square[r//3, c//3].add(board[r][c])
        return True