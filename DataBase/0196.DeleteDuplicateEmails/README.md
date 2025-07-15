# Delete Duplicate Emails

- Dificuldade: Fácil
- Status: Concluído
- [Descrição do problema no LeetCode](https://leetcode.com/problems/delete-duplicate-emails/)

## Enunciado
Escreva uma solução para excluir todos os e-mails duplicados, mantendo apenas um e-mail exclusivo com o menor id.

Para usuários de SQL, observe que você deve escrever uma DELETEinstrução e não uma SELECTúnica.

Para usuários do Pandas, observe que é necessário fazer modificações Personno local.

Após executar o script, a resposta exibida é a Persontabela. O driver primeiro compilará e executará o trecho de código e, em seguida, exibirá a Persontabela. A ordem final da Persontabela não importa .
---

## Código da solução

```
import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by='id',inplace=True)
    person["Duplicado"] = person['email'].duplicated() 
    person.drop(person[person["Duplicado"]==True].index,inplace=True)
    person.drop(columns=["Duplicado"], inplace=True)
```
## Lógica Para Chegar Na Resposta:

Primeiro, organizei a tabela para garantir que os dados com menor id viessem primeiro.
Depois, marquei os e-mails repetidos e removi as linhas que estavam duplicadas.
Por fim, retirei a coluna usada só para identificar os repetidos, deixando a tabela limpa.
