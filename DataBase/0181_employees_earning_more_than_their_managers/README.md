# Employees Earning More Than Their Managers

- Dificuldade: Fácil
- Status: Concluído
- [Descrição do problema no LeetCode](https://leetcode.com/problems/employees-earning-more-than-their-managers/)

## Enunciado
Escreva uma solução para encontrar os funcionários que ganham mais que seus gerentes.Retorna a tabela de resultados em qualquer ordem .O formato do resultado está no exemplo a seguir.

---

## Código da solução

```python
import pandas as pd
import pandas as pd



def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    chefes = employee[employee['managerId'].isnull()]
    chefes['managerId'] = chefes['id'] 
    novatabela = pd.merge(employee,chefes ,on ='managerId',how ='inner')
    novatabela = novatabela[novatabela['salary_x']>novatabela['salary_y']]
    novatabela = novatabela.rename(columns={'name_x':'Employee'})
    return novatabela[['Employee']]
```
## Lógica Para Chegar Na Resposta:

A abordagem inicial foi criar uma tabela auxiliar para identificar os funcionarios que possuiam chefes.Após isso, realizei um merge do tipo inner join entre o DataFrame original e essa tabela, conectando cada funcionário ao seu chefe
depois disso comparei os salários e filtrei apenas os funcionários que possuem salário maior que o de seus chefes. Por fim, a função retorna a lista desses funcionários.
