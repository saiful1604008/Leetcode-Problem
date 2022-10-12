class Solution {
public:
    bool isBipartite(vector<vector<int>>& graph) {
        vector<int>color(graph.size(), -1);
        
        for (int i = 0; i < graph.size(); i++){
            if (color[i] == -1){
                queue<int>q;
                q.push(i);
                color[i] = 0;
                
                while(!q.empty()){
                    int curr = q.front();
                    q.pop();
                    
                    for (auto x:graph[curr]){
                        if (color[x] == -1){
                            color[x] = 1 - color[curr];
                            q.push(x);
                        }
                        else if (color[x] == color[curr])
                            return false;                        
                    }
                }
            }
        }
        return true;
    }
};