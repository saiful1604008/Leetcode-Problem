class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        string_s = []
        for i in range(len(s)):
            if s[i] == '#':
                if len(string_s) != 0:
                    string_s.pop(-1)
            else:
                string_s.append(s[i])
        
        string_t = []
        for i in range(len(t)):
            if t[i] == '#':
                if len(string_t) != 0:
                    string_t.pop(-1)
            else:
                string_t.append(t[i])
        
        
        if string_s == string_t:
            return True
        else:
            return False