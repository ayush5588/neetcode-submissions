class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_mp = defaultdict(set)
        col_mp = defaultdict(set)
        sqr_mp = defaultdict(set)

        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == ".":
                    continue
                elif board[r][c] in row_mp[r]:
                    return False
                elif board[r][c] in col_mp[c]:
                    return False
                elif board[r][c] in sqr_mp[tuple([r//3,c//3])]:
                    return False
                else:
                    row_mp[r].add(board[r][c])
                    col_mp[c].add(board[r][c])
                    sqr_mp[tuple([r//3,c//3])].add(board[r][c])
        

        return True