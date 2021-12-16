class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return
        
        dicts = {'2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']
                }
        
        result = [""]
        temp = []
        
        for d in digits:
            char = dicts[d]
            for i in result:
                for j in char:
                    temp.append(i + j)
            
            result = temp
            temp = []
        return result
                