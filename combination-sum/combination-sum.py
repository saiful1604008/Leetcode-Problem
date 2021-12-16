class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def solve(i, total, list1):
            if total == target:
                return (result.append(list1.copy()))
            
            if i >= len(candidates) or total > target:
                return 
            
            list1.append(candidates[i])
            solve(i, total + candidates[i], list1)
            list1.pop()
            solve(i + 1, total, list1)
            
        solve(0,0,[])
        
        return result