class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        while len(stones) > 1:
            if stones[0] == stones[1] and len(stones) == 2:
                return 0
            elif stones[0] == stones[1]:
                stones.pop(0)
                stones.pop(0)
            elif stones[0] != stones[1]:
                stones[0] = stones[0] - stones[1]
                stones.pop(1)
            stones.sort(reverse=True)
        return stones[0]
        
                
                
        