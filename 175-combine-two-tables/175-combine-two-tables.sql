# Write your MySQL query statement below

SELECT firstName, lastName, city, state
From Person
Left Join Address
ON Person.personId = Address.personId