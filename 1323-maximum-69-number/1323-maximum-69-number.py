class Solution:
    def maximum69Number (self, num: int) -> int:
        count = 0
        num1 = str(num)
        res = ''
        
        for char in num1:
            if char == '6'and count == 0:
                res += '9'
                count += 1
            
            else:
                res += char
        
        return int(res)
        