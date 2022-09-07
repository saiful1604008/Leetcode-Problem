# Write your MySQL query statement below

select a1.id from weather as a1
INNER JOIN weather as a2
    ON
        datediff(a1.recordDate, a2.recordDate) = 1 
    and
        a1.temperature > a2.temperature 