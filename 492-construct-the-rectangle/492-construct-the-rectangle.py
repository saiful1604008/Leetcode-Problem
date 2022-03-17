class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        l = w = round(math.sqrt(area))
        
        while l*w != area:
            if l*w < area:
                l += 1
            else:
                w -= 1 
        
        return [l,w]
             
                