class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def solve(word):
            result, dict1 = [], {}
            i = 1
            for char in word:
                if char not in dict1:
                    dict1[char] = i
                    i += 1
                result.append(dict1[char])
            return result
        
        if solve(s) == solve(t):
            return True
        else:
            return False

        