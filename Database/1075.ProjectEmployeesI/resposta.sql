# Write your MySQL query statement below
SELECT project_id,ROUND(AVG(experience_years),2) AS average_years
FROM Project AS p
RIGHT JOIN Employee AS e
ON p.employee_id = e. employee_id
GROUP BY project_id
HAVING project_id IS NOT NULL
ORDER BY project_id
