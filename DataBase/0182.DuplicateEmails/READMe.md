# Duplicate Emails

- Dificuldade: Fácil
- Status: Concluído
- [Descrição do problema no LeetCode](https://leetcode.com/problems/duplicate-emails/description/)

## Enunciado
Escreva uma solução para relatar todos os e-mails duplicados. Observe que é garantido que o campo de e-mail não seja NULL.

Retorna a tabela de resultados em qualquer ordem .

O formato do resultado está no exemplo a seguir.

---

## Código da solução

```python
import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
   novoDataframe = person.copy()
   novoDataframe["Verificador"] = person['email'].duplicated()
   novoDataframe = novoDataframe[novoDataframe['Verificador'] == True]
   novoDataframe = novoDataframe.rename(columns={'email':'Email'})
   novoDataframe = novoDataframe.drop_duplicates(subset='Email')
   return novoDataframe[['Email']]
```
## Lógica Para Chegar Na Resposta:

Para chegar ao resultado correto primeiro adicionei uma coluna chamada Verificador responsável por identificar se havia outros registros com o mesmo e-mail.
Em seguida, filtrei apenas as linhas em que o verificador indicava que tinha duplicados.Por fim utilizei o método drop_duplicates para remover repetições e obter a resposta correta. 
Demorou um tempo considerável para chegar a esse raciocínio, mas nada impossível.
