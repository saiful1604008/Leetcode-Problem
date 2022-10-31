class Solution {
public:
    int earliestFullBloom(vector<int>& plantTime, vector<int>& growTime) {
        vector<pair<int,int>>v;
        
        for(int i=0; i<plantTime.size();i++){
            v.push_back({growTime[i], plantTime[i]});
        }
        
        sort(v.begin(), v.end());
        
        int time = 0, day=0;
        for(int i=plantTime.size()-1; i>=0; i--){
            time += v[i].second;
            day = max(day, time+v[i].first);
        }
        
        return day;
    }
};