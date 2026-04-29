class Solution(object):
    def isValidSudoku(self, board):
        
        rows = set()
        cols = set()
        boxes = set()
        
        for r in range(9):
            for c in range(9):
                
                num = board[r][c]
                
                if num == ".":
                    continue
                
                # identify which 3x3 box it belongs to
                box = (r // 3, c // 3)
                
                # duplicate found
                if ((r, num) in rows or
                    (c, num) in cols or
                    (box, num) in boxes):
                    return False
                
                rows.add((r, num))
                cols.add((c, num))
                boxes.add((box, num))
        
        return True