class Solution {
public:
    void bfs(int x,int y,vector<vector<int>> &vis,vector<vector<char>> &grid,vector<int> & dr,vector<int> &dc)
  {
      vis[x][y] = 1;
      queue<pair<int,int>> q;
      q.push({x,y});
        
      int n = grid.size();
      int m = grid[0].size();
      
      while(!q.empty()){
          int x = q.front().first;
          int y = q.front().second;
          q.pop();
          
          for(int i=0;i<4;i++)
        {
                  int nx=x+dr[i];
                  int ny=y+dc[i];
                  if(nx >=0 && nx <n && ny >= 0 && ny < m && grid[nx][ny] == '1' && !vis[nx][ny])
                  {
                      vis[nx][ny] = 1;
                      q.push({nx, ny});
                  }
              }
          }
      }
  
    
    int numIslands(vector<vector<char>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        
        int cnt = 0;
        vector<int> dr,dc;
        dr={-1,1,0,0};
        dc={0,0,-1,1}; 
        
        vector<vector<int>> vis(n,vector<int>(m,0));
        
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(!vis[i][j] && grid[i][j] == '1'){
                    cnt++;
                    bfs(i,j,vis,grid,dr,dc);
                }
            }
        }
        return cnt;
    }
};