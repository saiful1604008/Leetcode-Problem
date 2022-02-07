class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1]*n
        for i in range(0,m-1):
            updated_row = [1] * n
            for j in range(n-2,-1,-1):
                updated_row[j] = updated_row[j+1] + row[j]
            row = updated_row
        
        return row[0]
        
        