class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_row = {}
        seen_col = {}
        seen_square = {}

        num_rows = len(board)
        num_cols = len(board[0])

        # check each row
        for row in range(num_rows):
            seen_row.setdefault(row, set())

            for col in range(num_cols):
                space = board[row][col]
                index = (row // 3) * 3 + col // 3

                if space == '.':
                    continue

                seen_square.setdefault(index, set())

                if space in seen_row[row] or space in seen_square[index]:
                    return False
                
                seen_row[row].add(space)
                seen_square[index].add(space)

        # check each col           
        for col in range(num_cols):
            seen_col.setdefault(col, set())

            for row in range(num_rows):
                space = board[row][col]

                if space == '.':
                    continue
                
                if space in seen_col[col]:
                    return False
                
                seen_col[col].add(space)
               
        return True
        