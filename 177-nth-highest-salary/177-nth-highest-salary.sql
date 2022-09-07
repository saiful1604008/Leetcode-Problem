CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
set N = N - 1;

  RETURN (
    (SELECT distinct (salary)
    FROM Employee 
    ORDER BY salary desc limit N,1)
      

  );
  
END

