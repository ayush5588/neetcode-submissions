class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        mp_rows = defaultdict(set)
        mp_cols = defaultdict(set)
        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == ".":
                    continue
                if board[r][c] in mp_rows[r]:
                    return False
                elif board[r][c] in mp_cols[c]:
                    return False
                elif board[r][c] in mp_rows[tuple([r//3,c//3])]:
                    return False
                else:
                    mp_rows[r].add(board[r][c])
                    mp_cols[c].add(board[r][c])
                    mp_rows[tuple([r//3,c//3])].add(board[r][c])
        
        return True