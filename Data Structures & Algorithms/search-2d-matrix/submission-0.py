class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])-1
        i = 0 
        j = n
        while i<j:
            mid = (i+j)//2
            if matrix[mid][0]==target or matrix[mid][m]==target:
                return True
            elif matrix[mid][0]<target and matrix[mid][m]>target:
                l = 0
                r = m
                row = matrix[mid]
                while l<r:
                    c = (l+r)//2
                    if row[c] == target:
                        return True
                    elif row[c] > target:
                        r = c
                    else:
                        l = c+1
                return False
            elif matrix[mid][0]>target:
                j = mid
            elif matrix[mid][m]<target:
                i = mid+1
        return False 
            
        