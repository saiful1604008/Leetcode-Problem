class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        summ = 0
        
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i == j :
                    summ += mat[i][j]
        
        for i in range(len(mat)):
            for j in reversed(range(len(mat))):
                if i + j == len(mat) - 1:
                    summ += mat[i][j]
                
                    if i == j :
                        summ -= mat[i][j]
        return summ
                