# Write your MySQL query statement below
select s.product_id,p.product_name
from Sales s
left join Product p
on p.product_id = s.product_id
group by s.product_id,p.product_name
having min(sale_date) >= '2019-01-01' and max(sale_date) <= '2019-03-31'
