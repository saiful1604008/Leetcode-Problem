class Solution:
    def toLowerCase(self, s: str) -> str:
        string = ''
        for letter in s:
            asc = ord(letter)
            if asc in range(65,91):
                string = string+ chr(asc + 32)
            else:
                string = string + letter
                
        return string
    