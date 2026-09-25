class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # for checking rows
        for i in range(0,9):
            c = set()
            for j in range(0,9):
                num = board[i][j]
                if num in c:
                    return False
                elif num != ".":
                    c.add(num)
        # for checking columns
        for i in range(0,9):
            r = set()
            for j in range(0,9):
                num = board[j][i]
                if num in r:
                    return False
                elif num != ".":
                    r.add(num)   
        
        # for checking 3*3 boxes
        start_points = [(0,0), (0,3), (0,6),
                        (3,0), (3,3), (3,6),
                        (6,0), (6,3), (6,6)]
        for i,j in start_points:
            s = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    num = board[row][col]
                    if num in s:
                        return False
                    elif num != ".":
                        s.add(num)
        return True