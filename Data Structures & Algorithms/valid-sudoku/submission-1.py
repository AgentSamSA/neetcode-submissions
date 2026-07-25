class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_row = {}
        seen_col = {}
        seen_square = {}

        num_rows = len(board)
        num_cols = len(board[0])

        for row in range(num_rows):
            for col in range(num_cols):
                space = board[row][col]
                index = (row // 3) * 3 + col // 3

                if space == '.':
                    continue
                
                seen_row.setdefault(row, set())
                seen_col.setdefault(col, set())
                seen_square.setdefault(index, set())

                if space in seen_row[row] or space in seen_col[col] or space in seen_square[index]:
                    return False
                
                seen_row[row].add(space)
                seen_col[col].add(space)
                seen_square[index].add(space)
               
        return True
        