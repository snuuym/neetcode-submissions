class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        #check columns & rows &sub-boxes
        cols = defaultdict(set)
        rows = defaultdict(set)
        boxes = defaultdict(set)     
        for i in range(n):
            for j in range(n):
                curr = board[i][j]
                if curr != ".":
                    if (curr in cols[j] or curr in rows[i] or curr in boxes[(i//3)*3+j//3]):
                        return False
                    cols[j].add(curr)
                    rows[i].add(curr)
                    boxes[(i//3)*3+j//3].add(curr)
        return True

        
        # #check sub-boxes
        # for i in range(n):
        #     boxes = []
        #     for j in range():
        #         r = i//3
        #         c = j//3
        #         box = board[r][c]
        #         if box != ".":
        #             if box not in boxes:
        #                 boxes.append(box)
        #             else:
        #                 return False

        