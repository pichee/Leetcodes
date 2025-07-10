# Customers Who Never Order

- Dificuldade: Fácil
- Status: Concluído
- [Descrição do problema no LeetCode](https://leetcode.com/problems/customers-who-never-order/description/)

## Enunciado
Escreva uma solução para encontrar todos os clientes que nunca pedem nada.

Retorna a tabela de resultados em qualquer ordem .

O formato do resultado está no exemplo a seguir.

---

## Código da solução

```python
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    clientesPedido = pd.merge(orders,customers,right_on='id',left_on='customerId',how='inner')
    resposta = customers[~customers['id'].isin(clientesPedido['customerId'])]
    resposta = resposta.rename(columns={'name':'Customers'})
    return resposta[['Customers']]
```
## Lógica Para Chegar Na Resposta:

Para obter o resultado correto, primeiro realizei um join entre as duas tabelas.Após apliquei uma lógica para identificar para os clientes que o  id não estava presente na lista de customerId dos pedidos.Após isso renomei a coluna para customers e já obtive o resultado correto

