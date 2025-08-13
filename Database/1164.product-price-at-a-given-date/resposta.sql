# Write your MySQL query statement below
# Resposta da para melhorar para ganhar performace
with PrimeiraCamada as (
    select product_id,new_price,change_date
    from products
    where change_date <= '2019-08-16'
    ),
ColetarMaioresDatas as (
select product_id,max(change_date) as MaiorData
from PrimeiraCamada
group by product_id),

PegandoMaiorValor as (
select Products.product_id,Products.new_price,MaiorData
from ColetarMaioresDatas
Left join Products
on Products.product_id = ColetarMaioresDatas.product_id and MaiorData=change_date
)

select distinct Products.product_id,coalesce(PegandoMaiorValor.new_price, 10) AS price
from Products
Left join PegandoMaiorValor
on PegandoMaiorValor.product_id = Products.product_id
