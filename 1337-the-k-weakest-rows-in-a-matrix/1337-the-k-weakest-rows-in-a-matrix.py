class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        list = []
        dic = {}
        
        for i in mat:
            count = 0
            for j in i:
                if j == 1:
                    count += 1
            list.append(count)
        
        for i in range(len(list)):
            dic[i] = list[i]
        
        res = sorted(dic, key = dic.get)
        print(res)
        return res[:k]
        
        
            
        
            
        
