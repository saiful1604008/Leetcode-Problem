class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        x,y = len(matrix), len(matrix[0])
        left, right, down, upper = 0, y-1, x-1, 0
        
        while len(result) < x*y :
            for column in range(left, right+1):
                result.append(matrix[upper][column])
                
            for row in range(upper + 1, down + 1):
                result.append(matrix[row][right])
            
            if upper < down:  
                for column in range(right - 1, left - 1, -1):
                    result.append(matrix[down][column])
                    
            if left < right:  
                for row in range(down - 1, upper, -1):
                    result.append(matrix[row][left])
                    
            left = left + 1
            right = right - 1 
            down = down - 1
            upper = upper + 1
            
        return result
            