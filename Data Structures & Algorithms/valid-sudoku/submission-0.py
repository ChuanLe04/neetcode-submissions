class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        squares = {}

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == '.':
                    continue
                
                box_key = (r // 3, c // 3)

                if r not in rows:
                    rows[r] = set()
                if c not in cols:
                    cols[c] = set()
                if box_key not in squares:
                    squares[box_key] = set()

                #check if the number already exists in the current row, column or box
                if (val in rows[r] or val in cols[c] or val in squares[box_key]):
                    return False
                
                #otherwise, add it to the respective sets
                rows[r].add(val)
                cols[c].add(val)
                squares[box_key].add(val)

        return True
        

