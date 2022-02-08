class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seat_ = sorted(seats)
        student_ = sorted(students)
        res = 0
        for i in range(len(seat_)):
            res += abs(student_[i] - seat_[i])
            
        return res
        