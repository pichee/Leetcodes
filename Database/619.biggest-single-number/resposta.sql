with contador as (
    select num,count(num) as qtd
    from MyNumbers
    group by num
)
select max(num) as num
from contador
where qtd = 1
