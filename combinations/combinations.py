class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def solve(i=0, taken=[]):
            if len(taken) == k:
                res.append(taken[:])
                return
            
            for pos in range(i,n):
                taken.append(pos+1)
                solve(pos+1,taken)
                taken.pop()
                
        solve()
        return res