# Combine Two Tables

- Dificuldade: Fácil
- Status: Concluído
- [Descrição do problema no LeetCode](https://leetcode.com/problems/combine-two-tables/description/)

## Enunciado
Escreva uma solução para informar o nome, sobrenome, cidade e estado de cada pessoa na Persontabela. Se o endereço de uma pessoa personIdnão estiver presente na Addresstabela, informe null.

---

## Código da solução

```
import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
   merge = pd.merge(person,address , on='personId',how ='left')
   resultado = merge[['firstName','lastName','city','state']]
   return resultado
```
## Lógica Para Chegar Na Resposta:

Primeiro, juntei as duas tabelas usando o campo em comum para que as informações das pessoas ficassem junto com seus endereços.
Depois, escolhi só as colunas que realmente importavam para o resultado final: o nome, sobrenome, cidade e estado.
No final, a função retorna só essas informações.
