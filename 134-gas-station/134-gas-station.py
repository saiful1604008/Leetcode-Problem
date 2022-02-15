class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        idx, start = 0, 0
        if sum(cost) > sum(gas):
            return -1
        
        for i in range(len(gas)):
            idx = idx + gas[i] - cost[i]
            #print (idx)
            if idx < 0 :
                start = i + 1
                idx = 0
                
        return start