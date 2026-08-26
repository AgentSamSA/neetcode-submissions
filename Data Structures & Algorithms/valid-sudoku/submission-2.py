class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_row = {}
        seen_col = {}
        seen_box = {}

        rows = len(board)
        cols = len(board[0])

        for row in range(rows):
            seen_row.setdefault(row, set())
            for col in range(cols):
                space = board[row][col]
                seen_col.setdefault(col, set())

                index = (row // 3) * 3 + col // 3
                seen_box.setdefault(index, set())

                if space == '.':
                    continue
                
                if space in seen_row[row] or space in seen_col[col] or space in seen_box[index]:
                    return False
                
                seen_row[row].add(space)
                seen_col[col].add(space)
                seen_box[index].add(space)
        
        return True