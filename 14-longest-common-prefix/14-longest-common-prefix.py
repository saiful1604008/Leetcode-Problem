class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        str1 = strs[0]
        for i in range(len(str1)):
            for j in strs:
                if i == len(j) or j[i] != strs[0][i]:
                    return result
            result += strs[0][i]
        return result
                
        