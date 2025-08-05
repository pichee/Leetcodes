-- Write your PostgreSQL query statement below
Select event_day as day,emp_id,sum(out_time-in_time) as total_time
From Employees
Group by day,emp_id