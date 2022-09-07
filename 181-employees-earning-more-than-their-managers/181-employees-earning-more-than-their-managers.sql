# Write your MySQL query statement below

SELECT e1.name as Employee
From Employee as e1
Join Employee as mg
WHERE 
    e1.managerId = mg.id 
AND 
    e1.salary > mg.salary