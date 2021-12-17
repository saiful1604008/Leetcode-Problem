class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #r = s.strip()
        #result = s.strip().split(" ")
        return len(s.strip().split(" ")[-1])