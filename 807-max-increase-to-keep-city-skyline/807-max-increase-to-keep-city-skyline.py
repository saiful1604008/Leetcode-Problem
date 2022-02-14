class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        max_row , max_col = {}, {}
        res = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i not in max_row:
                    max_row[i] = grid[i][j]
                
                if j not in max_col:
                    max_col[j] = grid[i][j]
                
                max_row[i] = max(max_row[i], grid[i][j])
                max_col[j] = max(max_col[j], grid[i][j])
         
        #print (max_row)
        
        #print (max_col)       
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                minimum = min(max_row[i], max_col[j])
                if grid[i][j] < minimum:
                    res += minimum - grid[i][j]
        
        
        return res
                
                
    
                    