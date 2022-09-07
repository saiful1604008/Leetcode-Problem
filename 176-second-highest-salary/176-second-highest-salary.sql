# Write your MySQL query statement below


(select salary as SecondHighestSalary  from Employee 
group by salary 
order by  salary desc limit 1,1)

union

(select NULL)
limit 1;