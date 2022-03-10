class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    self.dfs(grid,i,j)
        return res
    
    
    def dfs(self, grid: List[List[str]], i,j):
        if i >= len(grid) or j >= len(grid[0]) or i <0 or j <0 or grid[i][j]!= '1':
            return 
        
        grid[i][j] = '0'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
        
        
        